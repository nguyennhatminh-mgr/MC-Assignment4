.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
	bipush 10
	newarray float
	astore_1
.var 2 is c I from Label0 to Label1
.var 3 is b F from Label0 to Label1
Label0:
	bipush 6
	invokestatic MCClass/foo(I)I
	invokestatic io/putInt(I)V
	bipush 10
	istore_2
	aload_1
	iconst_2
	aload_1
	iconst_1
	aload_1
	iconst_0
	bipush 10
	iload_2
	iadd
	i2f
	dup_x2
	fastore
	dup_x2
	fastore
	fastore
	aload_1
	iconst_0
	faload
	aload_1
	iconst_1
	faload
	fadd
	aload_1
	iconst_2
	faload
	fmul
	fstore_3
	fload_3
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 11
.limit locals 4
.end method

.method public static foo(I)I
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
	bipush 10
	ireturn
Label4:
	iconst_0
	ireturn
Label5:
Label1:
.limit stack 3
.limit locals 1
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
