.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x F from Label0 to Label1
.var 2 is y F from Label0 to Label1
.var 3 is z F from Label0 to Label1
.var 4 is a Z from Label0 to Label1
Label0:
	iconst_1
	istore 4
	ldc 4.5
	fstore_1
	ldc 1.3
	fstore_2
	ldc 5.6
	fstore_3
	iload 4
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label5:
	fload_1
	fload_2
	fmul
	fload_3
	fsub
	fload_1
	fload_1
	fmul
	fload_2
	fload_2
	fmul
	fsub
	fadd
	fstore_1
Label6:
Label4:
	fload_1
	fneg
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
