.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
Label0:
	aload_1
	iconst_4
	bipush 10
	iastore
	aload_1
	iconst_0
	invokestatic MCClass/func_arr()[I
	iconst_3
	iaload
	aload_1
	iconst_4
	iaload
	iadd
	iastore
	aload_1
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 9
.limit locals 2
.end method

.method public static func_arr()[I
.var 0 is a [I from Label0 to Label1
	bipush 10
	newarray int
	astore_0
Label0:
	aload_0
	iconst_3
	bipush 10
	iastore
	aload_0
	areturn
Label1:
.limit stack 4
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
