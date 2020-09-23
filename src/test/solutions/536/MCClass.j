.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is arr [Z from Label0 to Label1
	bipush 10
	newarray boolean
	astore_1
Label0:
	aload_1
	iconst_1
	iconst_1
	bastore
	aload_1
	iconst_2
	iconst_0
	bastore
	aload_1
	iconst_3
	aload_1
	iconst_1
	baload
	bastore
	aload_1
	iconst_4
	aload_1
	iconst_1
	baload
	aload_1
	iconst_2
	baload
	ior
	bastore
	aload_1
	iconst_3
	baload
	invokestatic io/putBoolLn(Z)V
	aload_1
	iconst_4
	baload
	invokestatic io/putBool(Z)V
Label1:
	return
.limit stack 18
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
