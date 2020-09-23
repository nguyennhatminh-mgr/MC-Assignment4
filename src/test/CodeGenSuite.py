import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    def test_int(self):
        """Simple program: int main() {} """
        input = """void main() {putInt(100);}"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],VoidType(),Block([
    			CallExpr(Id("putInt"),[IntLiteral(5)])]))])
    	expect = "5" 
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    def test_int_vardecl_local(self):
        """Simple program: int main() {} """
        input = """
                void main() {
                    int a; 
                    a=5;
                    putInt(100);
                }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_int_vardecl_global(self):
        """Simple program: int main() {} """
        input = """
                int a;
                void main() { 
                    a=5;
                    putInt(100);
                    int b;
                    
                }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_int_vardecl_local_with_block(self):
        """Simple program: int main() {} """
        input = """
                int a;
                void main() { 
                    a=5;
                    putInt(100);
                    {
                        int b,c,d;
                    }
                }"""
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_int_vardecl_in_func(self):
        """Simple program: int main() {} """
        input = """
                int a;
                void main() { 
                    a=5;
                    putInt(100);
                }
                void check(int c,int b){
                   int hello;
                   hello=5;
                }
                """
        expect = "100"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_float_in_func(self):
        """Simple program: int main() {} """
        input = """
                int a;
                void main() { 
                    a=5;
                    putFloat(100.4);
                }
                """
        expect = "100.4"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_boolean_in_func(self):
        """Simple program: int main() {} """
        input = """
                int a;
                void main() { 
                    a=5;
                    putBool(true);
                }
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_call_with_var_in_func(self):
        """Simple program: int main() {} """
        input = """
                int a;
                void main() { 
                    a=5;
                    putInt(a);
                }
                """
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_func_normal_call(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int b;
                    b=50;
                    hello(b);
                }
                void hello(int a){
                    putIntLn(a);
                }
                """
        expect = "50\n"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_binaryop_iadd(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int b;
                    b=50+4;
                    putInt(b);
                }
                """
        expect = "54"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_binaryop_imod(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int b;
                    b = 50 % 4;
                    putInt(b);
                }
                """
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_binaryop_iand(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    boolean b;
                    b = true && true;
                    putBool(b);
                }
                """
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_unaryop_negop(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int b;
                    b = -5;
                    putInt(b);
                }
                """
        expect = "-5"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_func_with_return(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    float b;
                    b = -5.4;
                    putFloat(b);
                }
                int hello(){
                    int a;
                    a=1;
                    return a;
                }
                """
        expect = "-5.4"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_func_with_return_and_callexpr(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int b;
                    b = hello();
                    putInt(b);
                }
                int hello(){
                    int a;
                    a=1;
                    return a;
                }
                """
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_func_call_with_string(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    string b;
                    b="hello";
                    putStringLn(b);
                }
                
                """
        expect = "hello\n"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_if_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int a;
                    a=13;
                    if(a>=10)
                        putInt(a);
                }
                
                """
        expect = "13"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_if_statement_have_else(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                    int a;
                    a=3;
                    if(a>=10)
                        putInt(a);
                    else{
                        putString("Have ELSE");
                    }
                }
                
                """
        expect = "Have ELSE"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_for_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int i;
                   for(i=0;i<5;i=i+1){
                       putInt(i);
                   }
                }
                
                """
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    def test_for_statement_with_break(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int i;
                   for(i=0;i<15;i=i+1){
                       putInt(i);
                       if(i==7) break;
                   }
                }
                
                """
        expect = "01234567"
        self.assertTrue(TestCodeGen.test(input,expect,520))

    def test_for_statement_with_continue(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int i;
                   for(i=0;i<10;i=i+1){
                       if(i==7) continue;
                       putInt(i);
                   }
                }
                
                """
        expect = "012345689"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    def test_dowhile_statement(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int i;
                   i=0;
                   do{
                       putInt(i);
                       i=i+1;
                   }
                   while(i<6);
                }
                
                """
        expect = "012345"
        self.assertTrue(TestCodeGen.test(input,expect,522))

    def test_dowhile_statement_with_break(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int i;
                   i=0;
                   do{
                       putInt(i);
                       i=i+1;
                       if(i==9)
                       {
                           {
                               break;
                           }
                       }
                   }
                   while(i<15);
                }
                
                """
        expect = "012345678"
        self.assertTrue(TestCodeGen.test(input,expect,523))

    def test_dowhile_statement_with_continue(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int i;
                   i=0;
                   do{
                        i=i+1;
                        if(i==10)
                        {
                            continue;
                        }
                        putInt(i);
                   }
                   while(i<15);
                }
                
                """
        expect = "1234567891112131415"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    def test_binaryop_with_sub_float(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   float i;
                   i= 8.3-3;
                   putFloat(i);
                }
                
                """
        expect = "5.3"
        self.assertTrue(TestCodeGen.test(input,expect,525))

    def test_arraycell(self):
        """Simple program: int main() {} """
        input = """
                void main() { 
                   int arr[10];
                   arr[4]=7+5;
                   putInt(arr[4]);
                }
                
                """
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,526))

    def test_arraycell_with_right_side(self):
    	input = """
        void main() {
            int arr[10];
            arr[4]=5;
            int b;
            b=arr[4]+1;
            putInt(b);
        }"""
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,527))

    def test_arraycell_with_right_side_many_operand(self):
    	input = """
        void main() {
            int arr[10];
            arr[4]=5;
            arr[5]=3;
            arr[6]=2;
            int b;
            b=arr[4]+arr[5]+arr[6];
            putInt(b);
        }"""
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_arraycell_with_both_side(self):
    	input = """
        void main() {
            int arr[10];
            arr[4]=5;
            arr[0]=arr[4]+5;
            putInt(arr[0]);
        }"""
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_arraycell_with_both_side_many(self):
    	input = """
        void main() {
            int arr[10];
            arr[4]=5;
            arr[1]=11;
            arr[2]=2;
            arr[0]=arr[4]+2+arr[1]+arr[2];
            putInt(arr[0]);
        }"""
    	expect = "20"
    	self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_arraycell_declare_with_float_type(self):
    	input = """
        void main() {
            float arr[10];
        }"""
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,531))

    def test_arraycell_declare_with_string_type(self):
    	input = """
        void main() {
            string arr[10];
        }"""
    	expect = ""
    	self.assertTrue(TestCodeGen.test(input,expect,532))

    def test_arraycell_with_string_type(self):
    	input = """
        void main() {
            string arr[10];
            arr[1]="hello";
            putString(arr[1]);
        }"""
    	expect = "hello"
    	self.assertTrue(TestCodeGen.test(input,expect,533))

    def test_arraycell_with_string_type_1(self):
    	input = """
        void main() {
            string arr[10];
            arr[1]="hello PPL";
            arr[2]=arr[1];
            putString(arr[2]);
        }"""
    	expect = "hello PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,534))

    def test_arraycell_with_bool_type(self):
    	input = """
        void main() {
            boolean arr[10];
            arr[1]=true;
            putBool(arr[1]);
        }"""
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,535))

    def test_arraycell_with_bool_type_many(self):
    	input = """
        void main() {
            boolean arr[10];
            arr[1]=true;
            arr[2]=false;
            arr[3]=arr[1];
            arr[4]=arr[1] || arr[2];
            putBoolLn(arr[3]);
            putBool(arr[4]);
        }"""
    	expect = "true\ntrue"
    	self.assertTrue(TestCodeGen.test(input,expect,536))

    def test_arraycell_with_float_type(self):
    	input = """
        void main() {
            float arr[10];
            arr[1]=3.444;
            putFloat(arr[1]);
        }"""
    	expect = "3.444"
    	self.assertTrue(TestCodeGen.test(input,expect,537))

    def test_arraycell_with_float_type_many(self):
    	input = """
        void main() {
            float arr[10];
            arr[1]=3.4;
            arr[2]=arr[1]+3;
            putFloat(arr[2]);
        }"""
    	expect = "6.4"
    	self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_arraycell_with_float_type_many_and_int(self):
    	input = """
        void main() {
            float arr[10];
            int arr1[5];
            arr[1]=3.4;
            arr1[0]=5;
            arr[2]=arr[1]+arr1[0];
            putFloat(arr[2]);
        }"""
    	expect = "8.4"
    	self.assertTrue(TestCodeGen.test(input,expect,539))

    def test_Funcdecl_after_main(self):
    	input ="""
        void main(){
                foo1();
            }
            void foo1(){
                putInt(3);
            }
        """
    	expect = "3"
    	self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_arraycell_global(self):
    	input ="""
        int arr[10];
        void main(){
                arr[0]=10;
                putInt(arr[0]);
            }
        """
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_function_return_array(self):
    	input ="""
        void main(){
            int arr[10];
            arr[4]=10;
            arr[0]=func_arr()[3]+arr[4];
            putInt(arr[0]);
        }
        int[] func_arr(){
            int a[10];
            a[3]=10;
            return a;
        }
        """
    	expect = "20"
    	self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_function_return_array_1(self):
    	input ="""
        void main(){
            float arr[10];
            arr[2]=func_arr()[3]+func_arr()[2];
            putFloat(arr[2]);
        }
        float[] func_arr(){
            float a[10];
            a[3]=10;
            a[2]=10;
            return a;
        }
        """
    	expect = "20.0"
    	self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_recursive_func_gt(self):
    	input ="""
        void main(){
            int a;
            a=gt(3);
            putInt(a);
        }
        int gt(int n){
            if(n==1)
                return 1;
            else return n*gt(n-1);
        }
        """
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_recursive_func_gt_with_block(self):
    	input ="""
        void main(){
            int a;
            a=gt(3);
            putInt(a);
        }
        int gt(int n){
            if(n==1){
                return 1;
            }
            else{
                return n*gt(n-1);
            } 
        }
        """
    	expect = "6"
    	self.assertTrue(TestCodeGen.test(input,expect,545))

    def test_function_return_array_with_unaryop(self):
    	input ="""
        void main(){
            float arr[10];
            arr[1]=-gt(4)[4];
            putFloat(arr[1]);
        }
        float[] gt(int n){
            float arr[10];
            if(n>=10){
                putString("Index out of range");
            }
            else{
                arr[n]=n*n;
            }
            return arr;
        }
        """
    	expect = "-16.0"
    	self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_function_return_array_with_unaryop_type_int(self):
    	input ="""
        void main(){
            int arr[10];
            arr[1]=-gt(4)[4];
            putInt(arr[1]);
        }
        int[] gt(int n){
            int arr[10];
            if(n>=10){
                putString("Index out of range");
            }
            else{
                arr[n]=n*n;
            }
            return arr;
        }
        """
    	expect = "-16"
    	self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_function_return_array_with_unaryop_type_int_covert_to_float(self):
    	input ="""
        void main(){
            float arr[10];
            arr[1]=-gt(4)[4]+1;
            putFloat(arr[1]);
        }
        int[] gt(int n){
            int arr[10];
            if(n>=10){
                putString("Index out of range");
            }
            else{
                arr[n]=n*n;
            }
            return arr;
        }
        """
    	expect = "-15.0"
    	self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_function_return_array_string(self):
    	input ="""
        void main(){
            string a[20];
            a[3]=createString(10)[5];
            putString(a[3]);
        }
        string[] createString(int n){
            string s[30];
            if(n>=30){
                putString("Index out of range");
            }
            else{
                int i;
                for(i=0;i<n;i=i+1){
                    s[i]="PPL";
                }
            }
            return s;
        }
        """
    	expect = "PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,549))

    def test_function_return_array_int_assign_array_type(self):
    	input ="""
        void main(){
            int arr[10];
            arr=get_int(4,5);
            putInt(arr[0]);
        }
        int[] get_int(int n, int m){
            int arr[10];
            arr[0]=n;
            arr[1]=m;
            return arr;
        }
        """
    	expect = "4"
    	self.assertTrue(TestCodeGen.test(input,expect,550))

    def test_function_both_side_array_int_assign_array_type(self):
    	input ="""
        void main(){
            int arr[10];
            arr[0]=10;
            int arr1[10];
            arr1=arr;
            putInt(arr1[0]);
        }
        
        """
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,551))
    #test binary op complex
    def test_binaryop_complex(self):
    	input ="""
        void main(){
            int a;
            a=10;
            if (a>5){
                a=a+3*4/5;
            }
            putInt(a);
        }
        
        """
    	expect = "12"
    	self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_binaryop_complex_string(self):
    	input ="""
        void main(){
            string a;
            a="Hello PPL";
            int check;
            check=10;
            if (check>5){
                putInt(check);
            }
            else{
                putString(a);
            }
        }
        
        """
    	expect = "10"
    	self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_binaryop_complex_string_1(self):
    	input ="""
        void main(){
            string a;
            a="Hello PPL";
            int check;
            check=4;
            if (check>5){
                putInt(check);
            }
            else{
                putString(a);
            }
        }
        
        """
    	expect = "Hello PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_binaryop_complex_int_both_side(self):
    	input ="""
        void main(){
            int a;
            a=10;
            int b;
            b=11;
            a=a+b-6;
            putInt(a);
        }
        
        """
    	expect = "15"
    	self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_binaryop_complex_int_both_side_and_array(self):
    	input ="""
        void main(){
            int a,b,c;
            int arr[10];
            a=10;
            b=20;
            c=30;
            arr[0]=a*b-c;
            putInt(arr[0]);
        }
        
        """
    	expect = "170"
    	self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_binaryop_complex_float_both_side(self):
    	input ="""
        void main(){
            float a,b,c;
            float arr[10];
            a=1.0;
            b=2.4;
            c=3.2;
            arr[0]=a*b-c;
            putFloat(arr[0]);
        }
        
        """
    	expect = "-0.79999995"
    	self.assertTrue(TestCodeGen.test(input,expect,557))
    
    def test_binaryop_complex_float_side_left_and_int_side_right(self):
    	input ="""
        void main(){
            int a,b;
            float c;
            float arr[10];
            a=10;
            b=24;
            c=32;
            arr[0]=a*b-c;
            putFloat(arr[0]);
        }
        
        """
    	expect = "208.0"
    	self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_binaryop_complex_float_global(self):
    	input ="""
        float c;
        void main(){
            int a,b;
            float arr[10];
            a=10;
            b=24;
            c=32;
            arr[0]=a*b-c;
            putFloat(arr[0]);
        }
        
        """
    	expect = "208.0"
    	self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_binaryop_complex_float_array_global(self):
    	input ="""
        float c[20];
        void main(){
            int a,b;
            a=10;
            b=24;
            c[0]=a*b-20;
            putFloat(c[0]);
        }
        """
    	expect = "220.0"
    	self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_binaryop_complex_int_array_global(self):
    	input ="""
        int c[20];
        void main(){
            int a,b;
            a=10;
            b=24;
            c[0]=a*b-20;
            putIntLn(c[0]);
        }
        """
    	expect = "220\n"
    	self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_binaryop_complex_boolean_array(self):
    	input ="""
        void main(){
            boolean arr[10];
            arr[1]=true;
            arr[2]=false;
            if(arr[1]==true){
                putString("PPL is always right");
            }
            else{
                putBool(arr[2]);
            }
        }
        """
    	expect = "PPL is always right"
    	self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_binaryop_complex_boolean_array_global(self):
    	input ="""
        boolean arr[10];
        void main(){
            arr[1]=false;
            arr[2]=true;
            if(arr[1]==true){
                putString("PPL is always right");
            }
            else{
                putBool(arr[2]);
            }
        }
        """
    	expect = "true"
    	self.assertTrue(TestCodeGen.test(input,expect,563))

    #test if statement complex
    def test_if_statement_complex(self):
    	input ="""
        void main(){
            int a;
            a=1;
            if(a==1){
                if(a<2){
                    putString("a less than 2");
                }
                else{
                    putString("a greater than or equal 2");
                }
            }
        }
        """
    	expect = "a less than 2"
    	self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_if_statement_complex_1(self):
    	input ="""
        void main(){
            int a;
            a=4;
            if(a<=5){
                if(a<2){
                    putString("a less than 2");
                }
                else{
                    putString("a greater than or equal 2");
                }
            }
        }
        """
    	expect = "a greater than or equal 2"
    	self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_if_statement_complex_with_else(self):
    	input ="""
        void main(){
            int a;
            a=10;
            if(a<=5){
                if(a<2){
                    putString("a less than 2");
                }
                else{
                    putString("a greater than or equal 2");
                }
            }
            else{
                if(a==10){
                    putString("10 grade PPL");
                }
                else{
                    putString("Not 10 grade PPL");
                }
            }
        }
        """
    	expect = "10 grade PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_if_statement_complex_with_else_1(self):
    	input ="""
        void main(){
            int a;
            a=9;
            if(a<=5){
                if(a<2){
                    putString("a less than 2");
                }
                else{
                    putString("a greater than or equal 2");
                }
            }
            else{
                if(a==10){
                    putString("10 grade PPL");
                }
                else{
                    putString("Not 10 grade PPL");
                }
            }
        }
        """
    	expect = "Not 10 grade PPL"
    	self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_if_statement_complex_with_else_and_binaryop(self):
    	input ="""
        void main(){
            int a;
            a=1;
            if(a<=5){
                if(a<2){
                    a=a*a+a-5;
                    putInt(a);
                }
                else{
                    putString("a greater than or equal 2");
                }
            }
            else{
                if(a==10){
                    putString("10 grade PPL");
                }
                else{
                    a=(2*a*a)/(a+a);
                    putInt(a);
                }
            }
        }
        """
    	expect = "-3"
    	self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_if_statement_complex_with_else_and_binaryop_1(self):
    	input ="""
        void main(){
            int a;
            a=7;
            if(a<=5){
                if(a<2){
                    a=a*a+a-5;
                    putInt(a);
                }
                else{
                    putString("a greater than or equal 2");
                }
            }
            else{
                if(a==10){
                    putString("10 grade PPL");
                }
                else{
                    a=(2*a*a)/(a+a);
                    putInt(a);
                }
            }
        }
        """
    	expect = "7"
    	self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_if_statement_complex_with_else_and_binaryop_with_float(self):
    	input ="""
        void main(){
            float x,y,z;
            boolean a;
            a=true;
            x=4.5;
            y=1.3;
            z=5.6;
            if(a==true){
                x=x*y-z+(x*x-y*y);
            }
            putFloat(-x);
        }
        """
    	expect = "-18.81"
    	self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_if_statement_complex_with_else_and_binaryop_with_float_1(self):
    	input ="""
        void main(){
            float x,y,z;
            boolean a;
            a=true;
            x=4.545;
            y=1.333;
            z=5.667;
            if(a==true){
                x=x*y-z+(x*x-y*y);
            }
            putFloat(-x);
        }
        """
    	expect = "-19.271624"
    	self.assertTrue(TestCodeGen.test(input,expect,571))

    #test for statement complex
    def test_for_statement_complex(self):
    	input ="""
        void main(){
            int index;
            for(index=0;index<5;index=index+1){
                putStringLn("I LOVE PPL");
            }
        }
        """
    	expect = "I LOVE PPL\nI LOVE PPL\nI LOVE PPL\nI LOVE PPL\nI LOVE PPL\n"
    	self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_for_statement_complex_with_if(self):
    	input ="""
        void main(){
            int index;
            for(index=0;index<4;index=index+1){
                if(index==3){
                    putIntLn(index);
                }
                putIntLn(index*index);
            }
        }
        """
    	expect = "0\n1\n4\n3\n9\n"
    	self.assertTrue(TestCodeGen.test(input,expect,573))


    def test_for_statement_complex_with_if_and_double_for(self):
    	input ="""
        void main(){
            int index[10];
            index[0]=5;
            index[1]=10;
            index[2]=7;
            index[3]=6;
            index[4]=19;
            index[5]=23;
            index[6]=15;
            index[7]=18;
            index[8]=23;
            index[9]=16;
            int i,j;
            for(i=0;i<10;i=i+1){
                for(j=1;j<i;j=j+1){
                    if(index[i]<index[j]){
                        int temp;
                        temp=index[i];
                        index[i]=index[j];
                        index[j]=temp;
                    }
                }
            }
            for(i=0;i<10;i=i+1){
                putInt(index[i]);
                putString(" ");
            }
        }
        """
    	expect = "5 6 7 10 15 16 18 19 23 23 "
    	self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_for_statement_complex_with_if_and_break(self):
    	input ="""
        void main(){
            int index[10];
            boolean a;
            a=false;
            int i,j;
            for(i=0;i<10;i=i+1){
               if(!a){
                   putInt(i);
                   putString(" ");
               }
               if(i==4){
                   break;
               }
            }
            
        }
        """
    	expect = "0 1 2 3 4 "
    	self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_Function_Return_ArrayCell_hieu(self):
        input = """
            float foo(){
                int i;
                float arr[5];
                for(i = 0 ; i < 5; i = i + 1){
                    arr[i] = 10 - i;
                }
                return arr[2];
            }
            void main(){
                float a;
                a=foo();
                putFloat(a);
            }"""
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    #test dowhile statement complex
    def test_dowhile_statement_complex(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do{
                putString("Hello ");
            }
            {
                putString("PPL ");
                i=i+1;
            }
            while(i<5);
        }
        """
    	expect = "Hello PPL Hello PPL Hello PPL Hello PPL Hello PPL "
    	self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_dowhile_statement_complex_with_continue(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do
            {
                putString("PPL LOVER ");
                i=i+1;
                if(i==3){
                    {
                        continue;
                    }
                }
            }
            while(i<5);
        }
        """
    	expect = "PPL LOVER PPL LOVER PPL LOVER PPL LOVER PPL LOVER "
    	self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_Function_Return_ArrayCell_More_hieu(self):
        input = """
        float foo(){
            int i;
            int arr[5];
            for(i = 0 ; i < 5; i = i + 1){
                arr[i] = i + 10;
            }
            return arr[3];
        }
        void main(){
            putFloat(foo());
        }"""
        expect = "13.0"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_dowhile_statement_complex_with_break(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do
            {
                putString("PPL LOVER ");
                i=i+1;
                if(i==3){
                    {
                        break;
                    }
                }
            }
            while(i<5);
        }
        """
    	expect = "PPL LOVER PPL LOVER PPL LOVER "
    	self.assertTrue(TestCodeGen.test(input,expect,580))

    def test_Function_With_Param_ArrayCell_hieu(self):
        input = """
        int foo(int arr[]){
            int i;
            for(i = 0 ; i < 3; i = i + 1){
                arr[i] = i;
            }
            return arr[1];
        }
        void main(){
            int arr[3];
            putInt(foo(arr));
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_program_with_simple_Exp_And_hieu(self):
    	input = """
        void main() {
            boolean flag;
            flag = true && false;
            putBool(flag);
        }"""
    	expect = "false"
    	self.assertTrue(TestCodeGen.test(input,expect,582))

    def test_UnOp_NOT_More_hieu(self):
        input = """
        void main(){
            boolean a;
            boolean b;
            a = true;
            b = !a && true;
            if (b != true){
                putString("This is False");
            }
            return;
        }"""
        expect = "This is False"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_IfElse_with_Booleanliteral_hieu(self):
        input = """
        void main(){
            if (false){
                putString("This is False");
            }
            else{
                putString("This is True");
            }
            return;
        }"""
        expect = "This is True"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_Function_With_ArrayPoiterType_hieu(self):
        input = """
        int[] foo(){
            int i;
            int arr[3];
            for(i = 0 ; i < 3; i = i + 1){
                arr[i] = i + 1;
            }
            return arr;
        }
        void main(){
            putInt(foo()[1]);
        }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,585))
    #test scope
    def test_function_and_scope(self):
        input = """
      
        void main(){
            int main;
            main=1;
            putInt(main);
            {
                int main;
                main=100;
                putInt(main);
            }
            putInt(main);
        }"""
        expect = "11001"
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_function_and_scope_in_mc_file(self):
        input = """
        int i;
        int f(){
            return 200;
        }
        void main(){
            int main;
            main=f();
            putIntLn(main);
            {
                int main;
                int f,i;
                main=f=i=100;
                putIntLn(main);
                putIntLn(f);
                putIntLn(i);
            }
            putInt(main);
        }"""
        expect = "200\n100\n100\n100\n200"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    def test_Return_In_VoidType_Main_Function(self):
        input = """
        void func(){
            putFloat(5.3);
            return;
        }
        void main(){
            func();
            return;
        }"""
        expect = "5.3"
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_Function_With_ArrayPoiterType_And_ArrayCell_hieu(self): 
        input = """
        void main(){
            int x;
            x = 1;
            float a[5];
            int b[5];
            b[2] = 2;
            a[2]= 5;
            putFloat(a[b[2]]);
        }"""
        expect = "5.0"
        self.assertTrue(TestCodeGen.test(input,expect,589)) 

    def test_Function_With_ArrayPoiterType_And_ArrayCell_More_hieu(self):
        input = """
        int[] foo(int n){
            int arr[3];
            return arr;
        }
        void main(){
            int x;
            x = 1 ;
            int a[5];
            int b[5];
            b[2] = 2;
            a[2]= 5;
            foo(3)[1+x] = a[b[2]] + 3;
            putInt(foo(3)[1+x]);
        }"""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_SumFunction_Recursion(self):
        input = """
        // tinh tong tu 1 den n            
        int foo(int n){
            if(n == 1) {
                return 1;
            }
            else {
                return n + foo(n-1);
            }
        }
        void main(){
            int x;
            x = foo(10);
            putInt(x);
        }"""
        expect = "55"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_MulFunction_Recursion(self):
        input = """
        // tinh tich tu 1 den n            
        int foo(int n){
            if(n == 1) {
                return 1;
            }
            else {
                return n * foo(n-1);
            }
        }
        void main(){
            int x;
            x = foo(10);
            putInt(x);
        }"""
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_GCD_Recursion_hieu(self):
        input = """            
        int gcd(int a, int b){
            if(b == 0){
                return a;
            }
            return gcd(b, a % b);
        }
        void main(){
            putString("GCD of 9 and 6: ");
            putInt(gcd(9, 6));
        }"""
        expect = "GCD of 9 and 6: 3"
        self.assertTrue(TestCodeGen.test(input,expect,593))
    #test Float compare
    def test_compare_with_float_type(self):
        input = """           
        void main(){
            float a,b;
            a=1.4;
            b=5.6;
            if(a>b){
                putString("a > b");
            }
            else{
                putString("a < b");
            }
        }"""
        expect = "a < b"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_Return_In_DoWhile_hieu(self):
        input = """
        int foo(int a){
            do{
                a = a + 1 ;
                return a;
            }while(a <3);
        }
        void main(){
            putInt(foo(0));
        }"""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_Return_In_DoWhile_With_manyStmt_hieu(self):
        input = """
        int foo(int a){
            do
            {
            }
            {
                a = a + 2 ;
            }
            return a;
            {
            }
            while(a <3);
        }
        void main(){
            putInt(foo(0));
        }"""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    def test_compare_with_float_type_greater_than(self):
        input = """           
        void main(){
            float a,b;
            a=1.4;
            b=5.6;
            if(a>=b){
                putString("a >= b");
            }
            else{
                putString("a < b");
            }
        }"""
        expect = "a < b"
        self.assertTrue(TestCodeGen.test(input,expect,597))

    def test_compare_with_float_type_less_than(self):
        input = """           
        void main(){
            float a,b;
            a=1.4;
            b=5.6;
            if(a<b){
                putString("a < b");
            }
            else{
                putString("a > b");
            }
        }"""
        expect = "a < b"
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_ArrayCell_Float_Simple_hieu(self):
        input = """
        void main(){
            float arr[3];
            arr[0]= 1.2;
            arr[1] = 2;
            arr[2] = arr[0] * arr[1];
            putFloat(arr[2]);
        }"""
        expect = "2.4"
        self.assertTrue(TestCodeGen.test(input,expect,599))

    def test_ArrayCell_string_Simple_my(self):
        input = """
        void main(){
            int arr[100];
            int a;
            a=arr[0]=arr[1]=10;
            putInt(arr[0]);
            putInt(arr[1]);
            putInt(a);
        }"""
        expect = "101010"
        self.assertTrue(TestCodeGen.test(input,expect,600))

    def test_if_else_statement_huy(self):
        input = """
        void main(){
            putInt(foo(6));
            float arr[10];
            int c;
            c=10;
            arr[0]=arr[1]=arr[2]=10+c;
            float b;
            b=(arr[0]+arr[1])*arr[2];
            putFloat(b);
        }
        int foo(int a){
            if (a>5) return 10;
            else return 0;
        }"""
        expect = "10800.0"
        self.assertTrue(TestCodeGen.test(input,expect,601))

    # def test_Assign_With_Many_ArrayCell_and_variable_In_DoWhile_hieu(self):
    # 	input ="""
    #     void main(){
    #         int i;
    #         i = 0;
    #         int a, b;
    #         float arr[2];
    #         do{
    #             i = i + 1;
    #             if (i < 3) continue;
    #             arr[0] = arr[1] = a = b = i + 1 ;
    #         }while(i < 5);
    #         putFloat(arr[0] + a);
    #     }
    #     """
    # 	expect = "12.0"
    # 	self.assertTrue(TestCodeGen.test(input,expect,602))

    def test_Assign_With_Many_ArrayCell_and_variable_In_DoWhile_hieu(self):
    	input ="""
        void main(){
            int i;
            i=0;
            do putInt(3); i=i+1; while(i<4);
        }
        """
    	expect = "3333"
    	self.assertTrue(TestCodeGen.test(input,expect,603))

    def test_for_stmt_with_continue_complex_huy(self):
        input = """
        void main() {
            int i;
            int sum;
            sum = 0;
            for(i=0;i<10;i=i+1){
                if (i%2 ==0) i= i+2;
                else continue;
                sum = sum + i;
            }
            putInt(sum);
        }"""
        expect = "18"
        self.assertTrue(TestCodeGen.test(input, expect, 604))