.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is a I from Label0 to Label1
.var 3 is b I from Label0 to Label1
.var 4 is arr [F from Label0 to Label1
	iconst_2
	newarray float
	astore 4
Label0:
	iconst_0
	istore_1
Label4:
Label5:
	iload_1
	iconst_1
	iadd
	istore_1
	iload_1
	iconst_3
	if_icmpge Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
	ifle Label9
	goto Label2
Label9:
	aload 4
	iconst_1
	aload 4
	iconst_0
	iload_1
	iconst_1
	iadd
	dup
	istore_3
	dup
	istore_2
	i2f
	dup_x2
	fastore
	fastore
Label6:
Label2:
	iload_1
	iconst_5
	if_icmpge Label10
	iconst_1
	goto Label11
Label10:
	iconst_0
Label11:
	ifgt Label4
Label3:
	aload 4
	iconst_0
	faload
	iload_2
	i2f
	fadd
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 13
.limit locals 5
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
