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
	iconst_1
	iconst_4
	invokestatic MCClass/gt(I)[I
	iconst_4
	iaload
	ineg
	iastore
	aload_1
	iconst_1
	iaload
	invokestatic io/putInt(I)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static gt(I)[I
.var 0 is n I from Label0 to Label1
.var 1 is arr [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
Label0:
	iload_0
	bipush 10
	if_icmplt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	ldc "Index out of range"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
	goto Label5
Label4:
Label8:
	aload_1
	iload_0
	iload_0
	iload_0
	imul
	iastore
Label9:
Label5:
	aload_1
	areturn
Label1:
.limit stack 7
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
