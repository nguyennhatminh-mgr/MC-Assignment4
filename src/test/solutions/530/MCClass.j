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
	iconst_5
	iastore
	aload_1
	iconst_1
	bipush 11
	iastore
	aload_1
	iconst_2
	iconst_2
	iastore
	aload_1
	iconst_0
	aload_1
	iconst_4
	iaload
	iconst_2
	iadd
	aload_1
	iconst_1
	iaload
	iadd
	aload_1
	iconst_2
	iaload
	iadd
	iastore
	aload_1
	iconst_0
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 12
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
