.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a I from Label0 to Label1
Label0:
	bipush 7
	istore_1
	iload_1
	iconst_5
	if_icmpgt Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	iload_1
	iconst_2
	if_icmpge Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label10
Label12:
	iload_1
	iload_1
	imul
	iload_1
	iadd
	iconst_5
	isub
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label13:
	goto Label11
Label10:
Label14:
	ldc "a greater than or equal 2"
	invokestatic io/putString(Ljava/lang/String;)V
Label15:
Label11:
Label7:
	goto Label5
Label4:
Label16:
	iload_1
	bipush 10
	if_icmpne Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
	ifle Label20
Label22:
	ldc "10 grade PPL"
	invokestatic io/putString(Ljava/lang/String;)V
Label23:
	goto Label21
Label20:
Label24:
	iconst_2
	iload_1
	imul
	iload_1
	imul
	iload_1
	iload_1
	iadd
	idiv
	istore_1
	iload_1
	invokestatic io/putInt(I)V
Label25:
Label21:
Label17:
Label5:
Label1:
	return
.limit stack 11
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
