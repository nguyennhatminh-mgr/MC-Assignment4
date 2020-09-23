.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a Ljava/lang/String; from Label0 to Label1
.var 2 is check I from Label0 to Label1
Label0:
	ldc "Hello PPL"
	astore_1
	iconst_4
	istore_2
	iload_2
	iconst_5
	if_icmple Label2
	iconst_1
	goto Label3
Label2:
	iconst_0
Label3:
	ifle Label4
Label6:
	iload_2
	invokestatic io/putInt(I)V
Label7:
	goto Label5
Label4:
Label8:
	aload_1
	invokestatic io/putString(Ljava/lang/String;)V
Label9:
Label5:
Label1:
	return
.limit stack 5
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
