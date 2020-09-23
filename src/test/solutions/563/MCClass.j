.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static arr [Z

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	getstatic MCClass/arr [Z
	iconst_1
	iconst_0
	bastore
	getstatic MCClass/arr [Z
	iconst_2
	iconst_1
	bastore
	getstatic MCClass/arr [Z
	iconst_1
	baload
	iconst_1
	if_icmpne Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	ldc "PPL is always right"
	invokestatic io/putString(Ljava/lang/String;)V
Label7:
	goto Label5
Label4:
Label8:
	getstatic MCClass/arr [Z
	iconst_2
	baload
	invokestatic io/putBool(Z)V
Label9:
Label5:
Label1:
	return
.limit stack 13
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
	bipush 10
	newarray boolean
	putstatic MCClass/arr [Z
Label1:
	return
.limit stack 1
.limit locals 0
.end method
