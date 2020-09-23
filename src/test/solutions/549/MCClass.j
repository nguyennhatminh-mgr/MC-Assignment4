.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [Ljava/lang/String; from Label0 to Label1
	bipush 20
	anewarray java/lang/String
	astore_1
Label0:
	aload_1
	iconst_3
	bipush 10
	invokestatic MCClass/createString(I)[Ljava/lang/String;
	iconst_5
	aaload
	aastore
	aload_1
	iconst_3
	aaload
	invokestatic io/putString(Ljava/lang/String;)V
Label1:
	return
.limit stack 5
.limit locals 2
.end method

.method public static createString(I)[Ljava/lang/String;
.var 0 is n I from Label0 to Label1
.var 1 is s [Ljava/lang/String; from Label0 to Label1
	bipush 30
	anewarray java/lang/String
	astore_1
Label0:
	iload_0
	bipush 30
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
.var 2 is i I from Label8 to Label9
Label8:
	iconst_0
	istore_2
Label12:
	iload_2
	iload_0
	if_icmpge Label13
	iconst_1
	goto Label14
Label13:
	iconst_0
Label14:
	ifle Label11
Label15:
	aload_1
	iload_2
	ldc "PPL"
	aastore
Label16:
Label10:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label12
Label11:
Label9:
Label5:
	aload_1
	areturn
Label1:
.limit stack 9
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
