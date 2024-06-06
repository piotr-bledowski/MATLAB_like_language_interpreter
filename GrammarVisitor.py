# Generated from Grammar.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser

# This class defines a complete generic visitor for a parse tree produced by GrammarParser.

class GrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by GrammarParser#program.
    def visitProgram(self, ctx:GrammarParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#addition.
    def visitAddition(self, ctx:GrammarParser.AdditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#subtraction.
    def visitSubtraction(self, ctx:GrammarParser.SubtractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#multiplication.
    def visitMultiplication(self, ctx:GrammarParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#matmul.
    def visitMatmul(self, ctx:GrammarParser.MatmulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#dot_product.
    def visitDot_product(self, ctx:GrammarParser.Dot_productContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#sin.
    def visitSin(self, ctx:GrammarParser.SinContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#cos.
    def visitCos(self, ctx:GrammarParser.CosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#sqrt.
    def visitSqrt(self, ctx:GrammarParser.SqrtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#root.
    def visitRoot(self, ctx:GrammarParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#log.
    def visitLog(self, ctx:GrammarParser.LogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#vector.
    def visitVector(self, ctx:GrammarParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#matrix.
    def visitMatrix(self, ctx:GrammarParser.MatrixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#trig_func.
    def visitTrig_func(self, ctx:GrammarParser.Trig_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#scalar_op.
    def visitScalar_op(self, ctx:GrammarParser.Scalar_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#operation.
    def visitOperation(self, ctx:GrammarParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#built_in_func.
    def visitBuilt_in_func(self, ctx:GrammarParser.Built_in_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#expression.
    def visitExpression(self, ctx:GrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#exp_func.
    def visitExp_func(self, ctx:GrammarParser.Exp_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#abs_func.
    def visitAbs_func(self, ctx:GrammarParser.Abs_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#ceil_func.
    def visitCeil_func(self, ctx:GrammarParser.Ceil_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#floor_func.
    def visitFloor_func(self, ctx:GrammarParser.Floor_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arcsin_func.
    def visitArcsin_func(self, ctx:GrammarParser.Arcsin_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arccos_func.
    def visitArccos_func(self, ctx:GrammarParser.Arccos_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#arctan_func.
    def visitArctan_func(self, ctx:GrammarParser.Arctan_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#sinh_func.
    def visitSinh_func(self, ctx:GrammarParser.Sinh_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#cosh_func.
    def visitCosh_func(self, ctx:GrammarParser.Cosh_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#factorial_func.
    def visitFactorial_func(self, ctx:GrammarParser.Factorial_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#modulo_op.
    def visitModulo_op(self, ctx:GrammarParser.Modulo_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#params.
    def visitParams(self, ctx:GrammarParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#param.
    def visitParam(self, ctx:GrammarParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#empty.
    def visitEmpty(self, ctx:GrammarParser.EmptyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statements.
    def visitStatements(self, ctx:GrammarParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#statement.
    def visitStatement(self, ctx:GrammarParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#assignment_statement.
    def visitAssignment_statement(self, ctx:GrammarParser.Assignment_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#func_statement.
    def visitFunc_statement(self, ctx:GrammarParser.Func_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#if_statement.
    def visitIf_statement(self, ctx:GrammarParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#else_statement.
    def visitElse_statement(self, ctx:GrammarParser.Else_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#for_statement.
    def visitFor_statement(self, ctx:GrammarParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#print_statement.
    def visitPrint_statement(self, ctx:GrammarParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#condition.
    def visitCondition(self, ctx:GrammarParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#logic_op.
    def visitLogic_op(self, ctx:GrammarParser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable.
    def visitVariable(self, ctx:GrammarParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_scalar.
    def visitVariable_scalar(self, ctx:GrammarParser.Variable_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_vec.
    def visitVariable_vec(self, ctx:GrammarParser.Variable_vecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by GrammarParser#variable_mat.
    def visitVariable_mat(self, ctx:GrammarParser.Variable_matContext):
        return self.visitChildren(ctx)



del GrammarParser