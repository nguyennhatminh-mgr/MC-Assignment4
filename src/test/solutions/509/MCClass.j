.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is b I from Label0 to Label1
Label0:
	bipush 50
	istore_1
	iload_1
	invokestatic MCClass/hello(I)V
Label1:
	return
.limit stack 2
.limit locals 2
.end method

.method public static hello(I)V
.var 0 is a I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 1
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
