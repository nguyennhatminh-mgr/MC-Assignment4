.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [F from Label0 to Label1
	bipush 10
	newarray float
	astore_1
Label0:
	aload_1
	iconst_2
	invokestatic MCClass/func_arr()[F
	iconst_3
	faload
	invokestatic MCClass/func_arr()[F
	iconst_2
	faload
	fadd
	fastore
	aload_1
	iconst_2
	faload
	invokestatic io/putFloat(F)V
Label1:
	return
.limit stack 7
.limit locals 2
.end method

.method public static func_arr()[F
.var 0 is a [F from Label0 to Label1
	bipush 10
	newarray float
	astore_0
Label0:
	aload_0
	iconst_3
	bipush 10
	i2f
	fastore
	aload_0
	iconst_2
	bipush 10
	i2f
	fastore
	aload_0
	areturn
Label1:
.limit stack 6
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
