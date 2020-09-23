.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is index [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
.var 2 is a Z from Label0 to Label1
.var 3 is i I from Label0 to Label1
.var 4 is j I from Label0 to Label1
Label0:
	iconst_0
	istore_2
	iconst_0
	istore_3
Label4:
	iload_3
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iload_2
	ifgt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label11
Label12:
	iload_3
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label13:
Label11:
	iload_3
	iconst_4
	if_icmpne Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label16
Label17:
	goto Label3
Label18:
Label16:
Label8:
Label2:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label4
Label3:
Label1:
	return
.limit stack 13
.limit locals 5
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
