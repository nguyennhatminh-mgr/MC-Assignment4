.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
	bipush 10
	newarray float
	astore_1
.var 2 is arr1 [I from Label0 to Label1
	iconst_5
	newarray int
	astore_2
Label0:
	aload_1
	iconst_1
	ldc 3.4
	fastore
	aload_2
	iconst_0
	iconst_5
	iastore
	aload_1
	iconst_2
	aload_1
	iconst_1
	faload
	aload_2
	iconst_0
	iaload
	i2f
	fadd
	fastore
	aload_1
	iconst_2
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 11
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
Label1:
	return
.limit stack 0
.limit locals 0
.end method
