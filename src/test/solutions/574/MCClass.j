.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is index [I from Label0 to Label1
	bipush 10
	newarray int
	astore_1
.var 2 is i I from Label0 to Label1
.var 3 is j I from Label0 to Label1
Label0:
	aload_1
	iconst_0
	iconst_5
	iastore
	aload_1
	iconst_1
	bipush 10
	iastore
	aload_1
	iconst_2
	bipush 7
	iastore
	aload_1
	iconst_3
	bipush 6
	iastore
	aload_1
	iconst_4
	bipush 19
	iastore
	aload_1
	iconst_5
	bipush 23
	iastore
	aload_1
	bipush 6
	bipush 15
	iastore
	aload_1
	bipush 7
	bipush 18
	iastore
	aload_1
	bipush 8
	bipush 23
	iastore
	aload_1
	bipush 9
	bipush 16
	iastore
	iconst_0
	istore_2
Label4:
	iload_2
	bipush 10
	if_icmpge Label5
	iconst_1
	goto Label6
Label5:
	iconst_0
Label6:
	ifle Label3
Label7:
	iconst_1
	istore_3
Label11:
	iload_3
	iload_2
	if_icmpge Label12
	iconst_1
	goto Label13
Label12:
	iconst_0
Label13:
	ifle Label10
Label14:
	aload_1
	iload_2
	iaload
	aload_1
	iload_3
	iaload
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label18
.var 4 is temp I from Label19 to Label20
Label19:
	aload_1
	iload_2
	iaload
	istore 4
	aload_1
	iload_2
	aload_1
	iload_3
	iaload
	iastore
	aload_1
	iload_3
	iload 4
	iastore
Label20:
Label18:
Label15:
Label9:
	iload_3
	iconst_1
	iadd
	istore_3
	goto Label11
Label10:
Label8:
Label2:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label4
Label3:
	iconst_0
	istore_2
Label23:
	iload_2
	bipush 10
	if_icmpge Label24
	iconst_1
	goto Label25
Label24:
	iconst_0
Label25:
	ifle Label22
Label26:
	aload_1
	iload_2
	iaload
	invokestatic io/putInt(I)V
	ldc " "
	invokestatic io/putString(Ljava/lang/String;)V
Label27:
Label21:
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label23
Label22:
Label1:
	return
.limit stack 42
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
