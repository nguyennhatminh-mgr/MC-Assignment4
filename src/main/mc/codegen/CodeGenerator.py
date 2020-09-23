'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [    Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName))
                ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)

class ClassType(Type):
    def __init__(self, cname):
        #cname: String
        self.cname = cname

    def __str__(self):
        return "ClassType"

    def accept(self, v, param):
        return v.visitClassType(self, param)

class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym
    #Minh them vo
    # def __str__(self):
    #     return "SubBody(" + str(self.frame) + ",[" + ','.join(str(i) for i in self.sym) + "])"

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst

class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        list_vardecl=[]
        for item in ast.decl:
            if type(item) is VarDecl:
                self.visit(item, e)
                list_vardecl.insert(0,Symbol(item.variable,self.visit(item.varType,c),CName(self.className)))
            else:
                isMain= item.name.name == "main" and len(item.param)==0 and type(item.returnType) is VoidType
                intype=[ArrayPointerType(StringType())] if isMain else [self.visit(x.varType,c) for x in item.param]
                self.env.insert(0,Symbol(item.name.name,MType(intype,item.returnType),CName(self.className)))
        list(map(lambda x:self.visit(x,SubBody(None,self.env)) if type(x) is not VarDecl else None,ast.decl))
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), None, Block(list())), c, Frame("<init>", VoidType))
        #generate function for static array global
        self.genMETHOD(FuncDecl(Id("<clinit>"), list(),None , Block(list())), list_vardecl, Frame("<clinit>", VoidType))
        self.emit.emitEPILOG()
        
        return c

    def genMETHOD(self, consdecl, o, frame):
        #consdecl: FuncDecl
        #o: Any
        #frame: Frame

        isInit = consdecl.returnType is None and consdecl.name.name=="<init>"
        # isMain = consdecl.name.name == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        isMain=consdecl.name.name == "main" and len(consdecl.param)==0 and type(consdecl.returnType) is VoidType

        isClinit=consdecl.name.name == "<clinit>"

        isFunc =(not isInit) and (not isMain) and (not isClinit)

        returnType = VoidType() if isInit else consdecl.returnType
        methodName = "<init>" if isInit else consdecl.name.name
        intype = [ArrayPointerType(StringType())] if isMain else [self.visit(x.varType,o) for x in consdecl.param]
        mtype = MType(intype, returnType)
        if isClinit:
            self.emit.printout(self.emit.emitMETHOD("<clinit>", MType([],VoidType()), isClinit, frame))
        else:
            self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            [self.visit(x,SubBody(frame,glenv)) for x in [ivar for ivar in consdecl.body.member if type(ivar) is VarDecl]]
        if isFunc:
            [self.visit(x,SubBody(frame,glenv)) for x in (consdecl.param+[ivar for ivar in consdecl.body.member if type(ivar) is VarDecl])]

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))

        # Generate code for statements
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        if isClinit:
            for item in glenv:
                if type(item.mtype) is ArrayType:
                    get_dimen=item.mtype.dimen
                    # self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
                    self.emit.printout(self.emit.emitPUSHICONST(int(get_dimen),frame))
                    self.emit.printout(self.emit.emitNEWARRAY(item.mtype.eleType,frame))
                    self.emit.printout(self.emit.emitPUTSTATIC(item.value.value+"/"+item.name,item.mtype,frame))
        
        # list(map(lambda x: self.visit(x, SubBody(frame, glenv)) if type(x) is not VarDecl else None, body.member))
        #moi them
        for item_func in body.member:
            if type(item_func) is BinaryOp:
                self.visitStatement(item_func,SubBody(frame,glenv))
            elif type(item_func) is not VarDecl:
                self.visit(item_func,SubBody(frame,glenv))
        
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        if isClinit:
            self.emit.printout(self.emit.emitRETURN(VoidType(),frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()

    def visitFuncDecl(self, ast, o):
        #ast: FuncDecl
        #o: Any
        
        subctxt = o
        frame = Frame(ast.name, ast.returnType)
        self.genMETHOD(ast, subctxt.sym.copy(), frame)
        # return SubBody(None, [Symbol(ast.name, MType(list(), ast.returnType), CName(self.className))] + subctxt.sym)
        return None

    def visitVarDecl(self,ast,o):
        frame=o.frame
        nenv=o.sym
        getType=self.visit(ast.varType,o)
        if frame is None: #vardecl in global
            nenv.insert(0,Symbol(ast.variable,getType,CName(self.className)))
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable,getType,False,""))
        else: #vardecl in function or block
            index=frame.getNewIndex()
            nenv.insert(0,Symbol(ast.variable,getType,Index(index)))
            self.emit.printout(self.emit.emitVAR(index,ast.variable,getType,frame.getStartLabel(),frame.getEndLabel(),frame))
            #declare for arraytype variable
            if type(getType) is ArrayType:
                get_dimen=ast.varType.dimen
                self.emit.printout(self.emit.emitPUSHICONST(int(get_dimen),frame))
                self.emit.printout(self.emit.emitNEWARRAY(getType.eleType,frame))
                self.emit.printout(self.emit.emitWRITEVAR(ast.variable,getType,index,frame))
        

    def visitBlock(self,ast,o):
        subtxt=o
        frame=subtxt.frame
        sym=subtxt.sym.copy()
        frame.enterScope(False)
        list(map(lambda x: self.visit(x,SubBody(frame,sym)) if type(x) is VarDecl else None,ast.member))
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(),frame))
        # get_list=list(map(lambda x: self.visit(x,SubBody(frame,sym)) if type(x) is not VarDecl else None,ast.member))
        get_list=[]
        for item in ast.member:
            if type(item) is BinaryOp:
                get_list.append(self.visitStatement(item,SubBody(frame,sym)))
            elif type(item) is not VarDecl:
                get_list.append(self.visit(item,SubBody(frame,sym)))
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(),frame))
        frame.exitScope()
        for x in get_list:
            if str(x)=="Return":
                return "Return"
        return None


    #--------------------------------------Statement---------------------------------#
    def visitStatement(self,ast,o):
        codeBin,typeBin=self.visit(ast,o)
        self.emit.printout(codeBin)
        

    def visitReturn(self,ast,o):
        if ast.expr is None:
            self.emit.printout(self.emit.emitRETURN(VoidType(),o.frame))
        else:
            rettype=o.frame.returnType
            ecode, etype=self.visit(ast.expr,Access(o.frame,o.sym,False,True))
            temp=""
            if type(ast.expr) is ArrayCell:
                ecode1,etype1=self.visit(ast.expr,Access(o.frame,o.sym,False,False))
                temp=ecode1
                etype=etype.eleType
            if type(rettype) is FloatType and type(etype) is IntType:
                self.emit.printout(ecode + temp + self.emit.emitI2F(o.frame) + self.emit.emitRETURN(rettype,o.frame))
            else:
                self.emit.printout(ecode+ temp + self.emit.emitRETURN(rettype,o.frame))
        return "Return"

    def visitIf(self,ast,o):
        ctxt=o
        frame=o.frame
        sym=o.sym
        expCode, expType= self.visit(ast.expr,Access(frame,ctxt.sym,False,True))
        labelELSE= frame.getNewLabel()
        labelEXIT= frame.getNewLabel() if ast.elseStmt else None
        self.emit.printout(expCode+self.emit.emitIFFALSE(labelELSE,frame))
        # thenStmt=self.visit(ast.thenStmt,ctxt) if type(ast.thenStmt) is not BinaryOp else self.visitStatement(ast.thenStmt,ctxt)
        thenStmt=""
        if type(ast.thenStmt) is BinaryOp:
            thenStmt=self.visitStatement(ast.thenStmt,Access(frame,sym,False,True))
        elif type(ast.thenStmt) is CallExpr:
            thenStmt=self.visit(ast.thenStmt,SubBody(frame,sym))
        else:
            thenStmt=self.visit(ast.thenStmt,Access(frame,sym,False,True))

        self.emit.printout(self.emit.emitGOTO(labelEXIT,frame)) if ast.elseStmt and str(thenStmt) != "Return" else None
        self.emit.printout(self.emit.emitLABEL(labelELSE,frame))
        elseStmt=""
        if ast.elseStmt:
            # elseStmt=self.visit(ast.elseStmt,ctxt) if type(ast.elseStmt) is not BinaryOp else self.visitStatement(ast.elseStmt,ctxt)
            if type(ast.elseStmt) is BinaryOp:
                elseStmt=self.visitStatement(ast.elseStmt,Access(frame,sym,False,True))
            elif type(ast.elseStmt) is CallExpr:
                elseStmt=self.visit(ast.elseStmt,SubBody(frame,sym))
            else:
                elseStmt=self.visit(ast.elseStmt,Access(frame,sym,False,True))
            
            self.emit.printout(self.emit.emitLABEL(labelEXIT,frame))

        if str(thenStmt) == "Return" and str(elseStmt) == "Return":
            return "Return"
        return None
            
    def visitFor(self,ast,o):
        ctxt=o
        frame=o.frame
        sym=o.sym

        frame.enterLoop()
        labelLoop=frame.getNewLabel()
        labelBreak=frame.getBreakLabel()
        labelContinue=frame.getContinueLabel()
        
        #Generate code for initial expr
        self.visit(ast.expr1, Access(frame,sym,False,True)) if type(ast.expr1) is not BinaryOp else self.visitStatement(ast.expr1,Access(frame,sym,False,True))

        #Generate code label to start loop
        self.emit.printout(self.emit.emitLABEL(labelLoop,frame))
        #Generate code for condition expr
        expr2Code, expr2Type=self.visit(ast.expr2,Access(frame,sym,False,True))
        self.emit.printout(expr2Code)
        self.emit.printout(self.emit.emitIFFALSE(labelBreak,frame))
        #Generate code for loop statement
        # self.visit(ast.loop,Access(frame,sym,False,True)) if type(ast.loop) is not BinaryOp else self.visitStatement(ast.loop,Access(frame,sym,False,True))
        # self.visit(ast.loop,ctxt) if type(ast.loop) is not BinaryOp else self.visitStatement(ast.loop,ctxt)
        
        if type(ast.loop) is BinaryOp:
            self.visitStatement(ast.loop,Access(frame,sym,False,True))
        elif type(ast.loop) is CallExpr:
            self.visit(ast.loop,SubBody(frame,sym))
        else:
            self.visit(ast.loop,Access(frame,sym,False,True))

        #Generate code for expression step or increase variable count
        self.emit.printout(self.emit.emitLABEL(labelContinue,frame))
        self.visit(ast.expr3, Access(frame,sym,False,True)) if type(ast.expr3) is not BinaryOp else self.visitStatement(ast.expr3,Access(frame,sym,False,True))
        #goto label loop if condition is still true
        self.emit.printout(self.emit.emitGOTO(labelLoop,frame))
        #generate label exit or label break to exit
        self.emit.printout(self.emit.emitLABEL(labelBreak,frame))

        frame.exitLoop()

        return None

    # def visitDowhile(self,ast,o):
    #     ctxt=o
    #     frame=o.frame
    #     sym=o.sym

    #     frame.enterLoop()
    #     labelLoop=frame.getNewLabel()
    #     breakLabel=frame.getBreakLabel()
    #     continueLabel=frame.getContinueLabel()
    #     #generate label continue or label to start loop
    #     self.emit.printout(self.emit.emitLABEL(labelLoop,frame))
    #     #generate code for body of dowhile statement
    #     temp=[self.visit(x,Access(frame,sym,False,True)) for x in ast.sl]
    #     #generate code for label continue
    #     self.emit.printout(self.emit.emitLABEL(continueLabel,frame))
    #     #generate code for condition in while
    #     expCode,expType= self.visit(ast.exp,Access(frame,sym,False,True))
    #     self.emit.printout(expCode)
    #     #check condition is true or false
    #     self.emit.printout(self.emit.emitIFFALSE(breakLabel,frame))
    #     #goto label continue if condition is still true
    #     self.emit.printout(self.emit.emitGOTO(labelLoop,frame))
    #     #generate label exit or label break to exit
    #     self.emit.printout(self.emit.emitLABEL(breakLabel,frame))
        
    #     frame.exitLoop()
        # for item in temp:
        #     if str(item) == "Return":
        #         return "Return"
        # return None           

    def visitDowhile(self,ast,o):
        ctxt=o
        frame=o.frame
        sym=o.sym

        frame.enterLoop()

        labelStart = frame.getNewLabel() #new
        breakLabel=frame.getBreakLabel()
        continueLabel=frame.getContinueLabel()
        #generate label continue or label to start loop
        # self.emit.printout(self.emit.emitLABEL(continueLabel,frame)) 
        self.emit.printout(self.emit.emitLABEL(labelStart,frame)) 
        #generate code for body of dowhile statement
        # temp=[self.visit(x,Access(frame,sym,False,True)) for x in ast.sl]
        temp=[]
        for item in ast.sl:
            if type(item) is BinaryOp:
                temp.append(self.visitStatement(item,Access(frame,sym,False,True)))
            elif type(item) is CallExpr:
                temp.append(self.visit(item,SubBody(frame,sym)))
            else:
                temp.append(self.visit(item,Access(frame,sym,False,True)))
        self.emit.printout(self.emit.emitLABEL(continueLabel,frame))        
        #generate code for condition in while
        expCode,expType= self.visit(ast.exp,Access(frame,sym,False,True))
        self.emit.printout(expCode)
        #check condition is true or false
        self.emit.printout(self.emit.emitIFTRUE(labelStart,frame))
        #goto label continue if condition is still true
        # self.emit.printout(self.emit.emitGOTO(continueLabel,frame))
        #generate label exit or label break to exit
        self.emit.printout(self.emit.emitLABEL(breakLabel,frame))        
        frame.exitLoop()
        if temp != []:
            for x in temp:
                if str(x)== "Return":
                    return "Return"
                else:
                    return None
        else:
            return None
    
    def visitBreak(self,ast,o):
        frame=o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getBreakLabel(),frame))

    def visitContinue(self,ast,o):
        frame=o.frame
        self.emit.printout(self.emit.emitGOTO(frame.getContinueLabel(),frame))

    #--------------------------------------Expression---------------------------------#


    def visitCallExpr(self, ast, o):
        #ast: CallExpr
        #o: Any

        ctxt = o
        frame = ctxt.frame
        nenv = ctxt.sym
        
        sym = self.lookup(ast.method.name, nenv, lambda x: x.name)
        cname = sym.value.value
    
        ctype = sym.mtype

        # in_ = ("", list())
        # for x in ast.param:
        #     str1, typ1 = self.visit(x, Access(frame, nenv, False, True))
        #     in_ = (in_[0] + str1, in_[1].append(typ1))
        # self.emit.printout(in_[0])
        # self.emit.printout(self.emit.emitINVOKESTATIC(cname + "/" + ast.method.name, ctype, frame))

        in_=""
        merge=list(zip(ctype.partype,ast.param))
        
        for x in merge:
            str1, typ1=self.visit(x[1],Access(frame,nenv,False,True))
            # if type(typ1) is ArrayType:
            if type(x[1]) is ArrayCell:
                str2,typ2= self.visit(x[1],Access(frame,nenv,False,False))
                str1+=str2
            if type(x[0]) is FloatType and type(typ1) is IntType:
                str1+=self.emit.emitI2F(frame)
            in_+=str1
            # if type(typ1) is ArrayPointerType:
            #     in_+=str2
        
        if type(ctxt) is SubBody:
            self.emit.printout(in_ + self.emit.emitINVOKESTATIC(cname+"/"+ast.method.name,ctype,frame)) 
            return "", ctype.rettype 
        if ctxt.isLeft==False and ctxt.isFirst==True:
            temp=in_ + self.emit.emitINVOKESTATIC(cname+"/"+ast.method.name,ctype,frame)
            return temp, ctype.rettype
        elif ctxt.isLeft==False and ctxt.isFirst==False:
            str_code, str_type=self.visit(ast.method,Access(frame,nenv,False,False))
            return str_code,str_type
        else:
            frame.push()
            str_code, str_type=self.visit(ast.method,Access(frame,nenv,True,False))
            return str_code,str_type
        
    def check_is_assign(self,type_to_check):
        if type(type_to_check) is BinaryOp:
            if type_to_check.op == '=':
                return True
        return False

    def visitBinaryOp(self,ast,o):
        ctxt=o
        frame=ctxt.frame
        nenv=ctxt.sym
        #visit assign
        if ast.op == "=":
            
            if self.check_is_assign(ast.right):
                rightCode, typeRight=self.visit(ast.right,Access(frame,nenv,False,False))
            else:
                rightCode, typeRight=self.visit(ast.right,Access(frame,nenv,False,True))
            leftCode, typeLeft=self.visit(ast.left,Access(frame,nenv,True,True))
            if type(typeRight) is not ArrayPointerType:
                if type(ast.right) is BinaryOp:
                    if ast.right.op != "=":
                        rightCode, typeRight=self.visit(ast.right,Access(frame,nenv,False,True))
                else:
                    rightCode, typeRight=self.visit(ast.right,Access(frame,nenv,False,True))

            if type(typeRight) in [ArrayType,ArrayPointerType]: #visit to load
                if type(ast.right) not in [CallExpr,Id]:
                    if not self.check_is_assign(ast.right):
                        rightCode1, typeRight1=self.visit(ast.right,Access(frame,nenv,False,False))
                        rightCode+=rightCode1
            #visit for many assign
            # if type(ast.right) is BinaryOp:
            #     if ast.right.op == "=":
            #         # temp=self.emit.emitDUP(frame)
            #         # rightCode+=temp
            #         self.visit(ast.right,Access(frame,nenv,False,False))
            #         # rightCode+=rightCode1

            temp_access=""
            if type(o) is Access:
                if o.isLeft==False and o.isFirst==False:
                    if type(ast.left) is not ArrayCell:
                        temp_access=self.emit.emitDUP(frame)
                    if type(ast.left) is ArrayCell:
                        temp_access=self.emit.emitDUPX2(frame)
                    # return temp,typeLeft
                    # rightCode+=temp_access

            if (type(typeLeft) is FloatType and type(typeRight) is IntType) :
                # self.emit.printout(rightCode+self.emit.emitI2F(frame)+leftCode)
                rightCode+=self.emit.emitI2F(frame)+temp_access+leftCode
            elif type(typeLeft) in [ArrayType,ArrayPointerType]:
                temp=""
                if type(typeLeft.eleType) is FloatType and type(typeRight) is IntType:
                    temp=self.emit.emitI2F(frame)
                if type(typeLeft.eleType) is FloatType and type(typeRight) in [ArrayType,ArrayPointerType]:
                    if type(typeRight.eleType) is IntType:
                        temp=self.emit.emitI2F(frame)
                
                if type(ast.left) is ArrayCell:
                    # if self.check_is_assign(ast.right):
                    #     self.emit.printout(leftCode)
                    # else:

                    # self.emit.printout(leftCode+rightCode+temp)
                    self.emit.printout(leftCode)

                    rightCode+=temp+temp_access
                    leftCode, typeLeft= self.visit(ast.left,Access(frame,nenv,True,False))
                    # self.emit.printout(leftCode)
                    rightCode+=leftCode
                else: #visit if lhs is array type
                    # self.emit.printout(rightCode+temp)
                    rightCode+=temp+temp_access
                    frame.push()
                    leftCode, typeLeft= self.visit(ast.left,Access(frame,nenv,True,True))
                    # self.emit.printout(leftCode)
                    rightCode+=leftCode
            else:
                # self.emit.printout(rightCode+leftCode)
                rightCode+=temp_access+ leftCode
            
            return rightCode,typeLeft
            # return None
        else:   # visit others
            leftCode, typeLeft=self.visit(ast.left,Access(frame,nenv,False,True))
            rightCode, typeRight=self.visit(ast.right,Access(frame,nenv,False,True))
            #visit second times for array cell
            if type(typeLeft) in [ArrayType,ArrayPointerType]:
                leftCode1, typeLeft1=self.visit(ast.left,Access(frame,nenv,False,False))
                leftCode+=leftCode1
                typeLeft=typeLeft.eleType
            if type(typeRight) in [ArrayType,ArrayPointerType]:
                rightCode1, typeRight1=self.visit(ast.right,Access(frame,nenv,False,False))
                rightCode+=rightCode1
                typeRight=typeRight.eleType
            #cast type
            if type(typeRight) is IntType and type(typeLeft) is FloatType:
                rightCode+=self.emit.emitI2F(frame)
                typeRight=FloatType()
            elif type(typeRight) is FloatType and type(typeLeft) is IntType:
                leftCode+=self.emit.emitI2F(frame)
                typeLeft=FloatType()
            
            if ast.op in ['+','-','*','/']:
                op_str=leftCode+rightCode
                op_str+=self.emit.emitADDOP(ast.op,typeLeft,frame) if ast.op in ['+','-'] else self.emit.emitMULOP(ast.op,typeLeft,frame)
                res_type=typeLeft
            elif ast.op == '%':
                op_str=leftCode+rightCode
                op_str += self.emit.emitMOD(frame)    
                res_type=IntType()
            elif ast.op in ['||','&&']:
                op_str=leftCode+rightCode
                op_str+= self.emit.emitANDOP(frame) if ast.op=='&&' else self.emit.emitOROP(frame)
                res_type=BoolType()
            elif ast.op in ['==','!=','>','<','>=','<=']:
                temp_new=self.emit.emitREOP(ast.op,typeLeft,frame)
                op_str=leftCode+rightCode+temp_new
                res_type=BoolType()

            return op_str,res_type

    def visitUnaryOp(self,ast,o):
        if type(o) is SubBody:
            expCode, expType=self.visit(ast.body, Access(o.frame,o.sym,False,True))
            if ast.op=='!':
                op_str=expCode+self.emit.emitNOT(expType,o.frame)
            elif ast.op=='-':
                op_str=expCode+self.emit.emitNEGOP(expType,o.frame)
            return op_str,expType
        #type o is Access and visit the first times
        if o.isLeft==False and o.isFirst==True:
            expCode, expType=self.visit(ast.body, Access(o.frame,o.sym,False,True))
            if type(expType) in [ArrayType,ArrayPointerType]: #array cell is return immediately, to the second visit, load data done, after visit op
                return expCode,expType
            else:
                if ast.op=='!':
                    op_str=expCode+self.emit.emitNOT(expType,o.frame)
                elif ast.op=='-':
                    op_str=expCode+self.emit.emitNEGOP(expType,o.frame)
                return op_str,expType
        else:   #visit the second times
            expCode, expType=self.visit(ast.body, Access(o.frame,o.sym,False,False))
            if ast.op=='!':
                op_str=expCode+self.emit.emitNOT(expType.eleType,o.frame)
            elif ast.op=='-':
                op_str=expCode+self.emit.emitNEGOP(expType.eleType,o.frame)
            return op_str,expType
            
    def visitId(self,ast,o):
        get_id=self.lookup(ast.name,o.sym,lambda x:x.name)
        if o.isFirst:
            if o.isLeft: #store
                if type(get_id.value) is CName:
                    return self.emit.emitPUTSTATIC(get_id.value.value+"/"+get_id.name,get_id.mtype,o.frame), get_id.mtype
                else:
                    return self.emit.emitWRITEVAR(get_id.name,get_id.mtype,get_id.value.value,o.frame) , get_id.mtype
            else:   #load
                if type(get_id.value) is CName:
                    return self.emit.emitGETSTATIC(get_id.value.value+"/"+get_id.name,get_id.mtype,o.frame), get_id.mtype
                else:
                    return self.emit.emitREADVAR(get_id.name,get_id.mtype,get_id.value.value,o.frame), get_id.mtype
        else:   #visit seconds times for array cell
            if o.isLeft: #store
                if type(get_id.mtype) is not MType:
                    get_type=get_id.mtype.eleType
                    return self.emit.emitWRITEVAR2(get_id.name,get_type,o.frame),get_id.mtype
                elif type(get_id.mtype) is MType:
                    get_type=get_id.mtype.rettype.eleType
                    return self.emit.emitWRITEVAR2(get_id.name,get_type,o.frame),get_id.mtype.rettype
            else: #load
                if type(get_id.mtype) is MType:
                    get_type=get_id.mtype.rettype.eleType
                    return self.emit.emitREADVAR2(get_id.name,get_type,o.frame),get_id.mtype.rettype
                else:
                    get_type=get_id.mtype.eleType
                    return self.emit.emitREADVAR2(get_id.name,get_type,o.frame),get_id.mtype

    def visitArrayCell(self,ast,o):
        frame=o.frame
        sym=o.sym
        
        if o.isFirst: #Lan 1 cho ca hai ben
            codeArr,typeArr=self.visit(ast.arr,Access(frame,sym,False,True))
            codeIdx,typeIdx=self.visit(ast.idx,Access(frame,sym,False,True))
            if type(ast.idx) is ArrayCell:
                codeArr1,typeArr1=self.visit(ast.idx,Access(frame,sym,False,False))
                codeIdx+=codeArr1
            
        elif o.isFirst==False and o.isLeft==True: #Ben trai va lan 2
            codeArr,typeArr=self.visit(ast.arr,Access(frame,sym,True,False))
            codeIdx=""
           
        elif o.isFirst==False and o.isLeft==False: #Ben phai va lan 2
            codeArr,typeArr=self.visit(ast.arr,Access(frame,sym,False,False))
            codeIdx=""
        
        return codeArr+codeIdx,typeArr
    
    #-----------------------------------Literals----------------------------------#
    def visitIntLiteral(self, ast, o):
        #ast: IntLiteral
        #o: Any
        ctxt = o
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()

    def visitFloatLiteral(self,ast,o):
        ctxt=o
        frame=ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value),frame), FloatType()

    def visitBooleanLiteral(self,ast,o):
        ctxt=o
        frame=ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value).lower(),frame), BoolType()

    def visitStringLiteral(self,ast,o):
        ctxt=o
        frame=ctxt.frame
        return self.emit.emitPUSHCONST(str(ast.value),StringType(),frame) , StringType()

    #---------------------------Type--------------------------------#
    def visitIntType(self, ast, o):
        return IntType()
    
    def visitFloatType(self, ast, o):
        return FloatType()
    
    def visitBoolType(self, ast, o):
        return BoolType()
    
    def visitStringType(self, ast, o):
        return StringType()
    
    def visitVoidType(self, ast, o):
        return VoidType()
    
    def visitArrayType(self, ast, o):
        return ArrayType(int(ast.dimen),self.visit(ast.eleType,o))

    def visitArrayPointerType(self,ast,o):
        return ArrayPointerType(self.visit(ast.eleType,o))