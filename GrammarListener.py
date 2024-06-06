# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete listener for a parse tree produced by GrammarParser.
class GrammarListener(ParseTreeListener):

    # Enter a parse tree produced by GrammarParser#program.
    def enterProgram(self, ctx:GrammarParser.ProgramContext):
        pass

    # Exit a parse tree produced by GrammarParser#program.
    def exitProgram(self, ctx:GrammarParser.ProgramContext):
        pass


    # Enter a parse tree produced by GrammarParser#addition.
    def enterAddition(self, ctx:GrammarParser.AdditionContext):
        pass

    # Exit a parse tree produced by GrammarParser#addition.
    def exitAddition(self, ctx:GrammarParser.AdditionContext):
        pass


    # Enter a parse tree produced by GrammarParser#subtraction.
    def enterSubtraction(self, ctx:GrammarParser.SubtractionContext):
        pass

    # Exit a parse tree produced by GrammarParser#subtraction.
    def exitSubtraction(self, ctx:GrammarParser.SubtractionContext):
        pass


    # Enter a parse tree produced by GrammarParser#multiplication.
    def enterMultiplication(self, ctx:GrammarParser.MultiplicationContext):
        pass

    # Exit a parse tree produced by GrammarParser#multiplication.
    def exitMultiplication(self, ctx:GrammarParser.MultiplicationContext):
        pass


    # Enter a parse tree produced by GrammarParser#modulo_op.
    def enterModulo_op(self, ctx:GrammarParser.Modulo_opContext):
        pass

    # Exit a parse tree produced by GrammarParser#modulo_op.
    def exitModulo_op(self, ctx:GrammarParser.Modulo_opContext):
        pass


    # Enter a parse tree produced by GrammarParser#matmul.
    def enterMatmul(self, ctx:GrammarParser.MatmulContext):
        pass

    # Exit a parse tree produced by GrammarParser#matmul.
    def exitMatmul(self, ctx:GrammarParser.MatmulContext):
        pass


    # Enter a parse tree produced by GrammarParser#mat_add.
    def enterMat_add(self, ctx:GrammarParser.Mat_addContext):
        pass

    # Exit a parse tree produced by GrammarParser#mat_add.
    def exitMat_add(self, ctx:GrammarParser.Mat_addContext):
        pass


    # Enter a parse tree produced by GrammarParser#mat_scalar_mult.
    def enterMat_scalar_mult(self, ctx:GrammarParser.Mat_scalar_multContext):
        pass

    # Exit a parse tree produced by GrammarParser#mat_scalar_mult.
    def exitMat_scalar_mult(self, ctx:GrammarParser.Mat_scalar_multContext):
        pass


    # Enter a parse tree produced by GrammarParser#dot_product.
    def enterDot_product(self, ctx:GrammarParser.Dot_productContext):
        pass

    # Exit a parse tree produced by GrammarParser#dot_product.
    def exitDot_product(self, ctx:GrammarParser.Dot_productContext):
        pass


    # Enter a parse tree produced by GrammarParser#vec_add.
    def enterVec_add(self, ctx:GrammarParser.Vec_addContext):
        pass

    # Exit a parse tree produced by GrammarParser#vec_add.
    def exitVec_add(self, ctx:GrammarParser.Vec_addContext):
        pass


    # Enter a parse tree produced by GrammarParser#vec_scalar_mult.
    def enterVec_scalar_mult(self, ctx:GrammarParser.Vec_scalar_multContext):
        pass

    # Exit a parse tree produced by GrammarParser#vec_scalar_mult.
    def exitVec_scalar_mult(self, ctx:GrammarParser.Vec_scalar_multContext):
        pass


    # Enter a parse tree produced by GrammarParser#sin.
    def enterSin(self, ctx:GrammarParser.SinContext):
        pass

    # Exit a parse tree produced by GrammarParser#sin.
    def exitSin(self, ctx:GrammarParser.SinContext):
        pass


    # Enter a parse tree produced by GrammarParser#cos.
    def enterCos(self, ctx:GrammarParser.CosContext):
        pass

    # Exit a parse tree produced by GrammarParser#cos.
    def exitCos(self, ctx:GrammarParser.CosContext):
        pass


    # Enter a parse tree produced by GrammarParser#sqrt.
    def enterSqrt(self, ctx:GrammarParser.SqrtContext):
        pass

    # Exit a parse tree produced by GrammarParser#sqrt.
    def exitSqrt(self, ctx:GrammarParser.SqrtContext):
        pass


    # Enter a parse tree produced by GrammarParser#root.
    def enterRoot(self, ctx:GrammarParser.RootContext):
        pass

    # Exit a parse tree produced by GrammarParser#root.
    def exitRoot(self, ctx:GrammarParser.RootContext):
        pass


    # Enter a parse tree produced by GrammarParser#log.
    def enterLog(self, ctx:GrammarParser.LogContext):
        pass

    # Exit a parse tree produced by GrammarParser#log.
    def exitLog(self, ctx:GrammarParser.LogContext):
        pass


    # Enter a parse tree produced by GrammarParser#vector.
    def enterVector(self, ctx:GrammarParser.VectorContext):
        pass

    # Exit a parse tree produced by GrammarParser#vector.
    def exitVector(self, ctx:GrammarParser.VectorContext):
        pass


    # Enter a parse tree produced by GrammarParser#matrix.
    def enterMatrix(self, ctx:GrammarParser.MatrixContext):
        pass

    # Exit a parse tree produced by GrammarParser#matrix.
    def exitMatrix(self, ctx:GrammarParser.MatrixContext):
        pass


    # Enter a parse tree produced by GrammarParser#trig_func.
    def enterTrig_func(self, ctx:GrammarParser.Trig_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#trig_func.
    def exitTrig_func(self, ctx:GrammarParser.Trig_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#scalar_op.
    def enterScalar_op(self, ctx:GrammarParser.Scalar_opContext):
        pass

    # Exit a parse tree produced by GrammarParser#scalar_op.
    def exitScalar_op(self, ctx:GrammarParser.Scalar_opContext):
        pass


    # Enter a parse tree produced by GrammarParser#vector_op.
    def enterVector_op(self, ctx:GrammarParser.Vector_opContext):
        pass

    # Exit a parse tree produced by GrammarParser#vector_op.
    def exitVector_op(self, ctx:GrammarParser.Vector_opContext):
        pass


    # Enter a parse tree produced by GrammarParser#matrix_op.
    def enterMatrix_op(self, ctx:GrammarParser.Matrix_opContext):
        pass

    # Exit a parse tree produced by GrammarParser#matrix_op.
    def exitMatrix_op(self, ctx:GrammarParser.Matrix_opContext):
        pass


    # Enter a parse tree produced by GrammarParser#operation.
    def enterOperation(self, ctx:GrammarParser.OperationContext):
        pass

    # Exit a parse tree produced by GrammarParser#operation.
    def exitOperation(self, ctx:GrammarParser.OperationContext):
        pass


    # Enter a parse tree produced by GrammarParser#built_in_func.
    def enterBuilt_in_func(self, ctx:GrammarParser.Built_in_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#built_in_func.
    def exitBuilt_in_func(self, ctx:GrammarParser.Built_in_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#exp_func.
    def enterExp_func(self, ctx:GrammarParser.Exp_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#exp_func.
    def exitExp_func(self, ctx:GrammarParser.Exp_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#abs_func.
    def enterAbs_func(self, ctx:GrammarParser.Abs_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#abs_func.
    def exitAbs_func(self, ctx:GrammarParser.Abs_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#ceil_func.
    def enterCeil_func(self, ctx:GrammarParser.Ceil_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#ceil_func.
    def exitCeil_func(self, ctx:GrammarParser.Ceil_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#floor_func.
    def enterFloor_func(self, ctx:GrammarParser.Floor_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#floor_func.
    def exitFloor_func(self, ctx:GrammarParser.Floor_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#arcsin_func.
    def enterArcsin_func(self, ctx:GrammarParser.Arcsin_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#arcsin_func.
    def exitArcsin_func(self, ctx:GrammarParser.Arcsin_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#arccos_func.
    def enterArccos_func(self, ctx:GrammarParser.Arccos_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#arccos_func.
    def exitArccos_func(self, ctx:GrammarParser.Arccos_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#arctan_func.
    def enterArctan_func(self, ctx:GrammarParser.Arctan_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#arctan_func.
    def exitArctan_func(self, ctx:GrammarParser.Arctan_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#sinh_func.
    def enterSinh_func(self, ctx:GrammarParser.Sinh_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#sinh_func.
    def exitSinh_func(self, ctx:GrammarParser.Sinh_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#cosh_func.
    def enterCosh_func(self, ctx:GrammarParser.Cosh_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#cosh_func.
    def exitCosh_func(self, ctx:GrammarParser.Cosh_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#factorial_func.
    def enterFactorial_func(self, ctx:GrammarParser.Factorial_funcContext):
        pass

    # Exit a parse tree produced by GrammarParser#factorial_func.
    def exitFactorial_func(self, ctx:GrammarParser.Factorial_funcContext):
        pass


    # Enter a parse tree produced by GrammarParser#params.
    def enterParams(self, ctx:GrammarParser.ParamsContext):
        pass

    # Exit a parse tree produced by GrammarParser#params.
    def exitParams(self, ctx:GrammarParser.ParamsContext):
        pass


    # Enter a parse tree produced by GrammarParser#param.
    def enterParam(self, ctx:GrammarParser.ParamContext):
        pass

    # Exit a parse tree produced by GrammarParser#param.
    def exitParam(self, ctx:GrammarParser.ParamContext):
        pass


    # Enter a parse tree produced by GrammarParser#empty.
    def enterEmpty(self, ctx:GrammarParser.EmptyContext):
        pass

    # Exit a parse tree produced by GrammarParser#empty.
    def exitEmpty(self, ctx:GrammarParser.EmptyContext):
        pass


    # Enter a parse tree produced by GrammarParser#statements.
    def enterStatements(self, ctx:GrammarParser.StatementsContext):
        pass

    # Exit a parse tree produced by GrammarParser#statements.
    def exitStatements(self, ctx:GrammarParser.StatementsContext):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx:GrammarParser.StatementContext):
        pass

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx:GrammarParser.StatementContext):
        pass


    # Enter a parse tree produced by GrammarParser#assignment_statement.
    def enterAssignment_statement(self, ctx:GrammarParser.Assignment_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#assignment_statement.
    def exitAssignment_statement(self, ctx:GrammarParser.Assignment_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#func_statement.
    def enterFunc_statement(self, ctx:GrammarParser.Func_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#func_statement.
    def exitFunc_statement(self, ctx:GrammarParser.Func_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#if_statement.
    def enterIf_statement(self, ctx:GrammarParser.If_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#if_statement.
    def exitIf_statement(self, ctx:GrammarParser.If_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#else_statement.
    def enterElse_statement(self, ctx:GrammarParser.Else_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#else_statement.
    def exitElse_statement(self, ctx:GrammarParser.Else_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#for_statement.
    def enterFor_statement(self, ctx:GrammarParser.For_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#for_statement.
    def exitFor_statement(self, ctx:GrammarParser.For_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#print_statement.
    def enterPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        pass

    # Exit a parse tree produced by GrammarParser#print_statement.
    def exitPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        pass


    # Enter a parse tree produced by GrammarParser#condition.
    def enterCondition(self, ctx:GrammarParser.ConditionContext):
        pass

    # Exit a parse tree produced by GrammarParser#condition.
    def exitCondition(self, ctx:GrammarParser.ConditionContext):
        pass


    # Enter a parse tree produced by GrammarParser#logic_op.
    def enterLogic_op(self, ctx:GrammarParser.Logic_opContext):
        pass

    # Exit a parse tree produced by GrammarParser#logic_op.
    def exitLogic_op(self, ctx:GrammarParser.Logic_opContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx:GrammarParser.VariableContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable.
    def exitVariable(self, ctx:GrammarParser.VariableContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable_scalar.
    def enterVariable_scalar(self, ctx:GrammarParser.Variable_scalarContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable_scalar.
    def exitVariable_scalar(self, ctx:GrammarParser.Variable_scalarContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable_vec.
    def enterVariable_vec(self, ctx:GrammarParser.Variable_vecContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable_vec.
    def exitVariable_vec(self, ctx:GrammarParser.Variable_vecContext):
        pass


    # Enter a parse tree produced by GrammarParser#variable_mat.
    def enterVariable_mat(self, ctx:GrammarParser.Variable_matContext):
        pass

    # Exit a parse tree produced by GrammarParser#variable_mat.
    def exitVariable_mat(self, ctx:GrammarParser.Variable_matContext):
        pass



del GrammarParser