.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	iconst_1
	ireturn
Label7:
Label4:
Label8:
	iload_0
	iload_0
	iconst_1
	isub
	invokestatic MCClass/foo(I)I
	iadd
	ireturn
Label9:
Label5:
Label1:
.limit stack 5
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
Label0:
	bipush 10
	invokestatic MCClass/foo(I)I
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 2
.limit locals 2
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
