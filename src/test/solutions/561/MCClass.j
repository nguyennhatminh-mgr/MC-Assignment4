.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static c [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
.var 2 is b I from Label0 to Label1
Label0:
	bipush 10
	istore_1
	bipush 24
	istore_2
	getstatic MCClass/c [I
	iconst_0
	iload_1
	iload_2
	imul
	bipush 20
	isub
	iastore
	getstatic MCClass/c [I
	iconst_0
	iaload
	invokestatic io/putIntLn(I)V
Label1:
	return
.limit stack 7
.limit locals 3
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
	bipush 20
	newarray int
	putstatic MCClass/c [I
Label1:
	return
.limit stack 1
.limit locals 0
.end method
