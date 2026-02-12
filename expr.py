from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

from my_token import Token


class Expr(ABC):
    @abstractmethod
    def accept(self, visitor: ExprVisitor):
        pass


class ExprVisitor[T](ABC):
    @abstractmethod
    def visitBinaryExpr(self, expr: BinaryExpr) -> T:
        pass

    @abstractmethod
    def visitUnaryExpr(self, expr: UnaryExpr) -> T:
        pass

    @abstractmethod
    def visitGroupingExpr(self, expr: GroupingExpr) -> T:
        pass

    @abstractmethod
    def visitLiteralExpr(self, expr: LiteralExpr) -> T:
        pass


@dataclass
class BinaryExpr(Expr):
    left: Expr
    operator: Token
    right: Expr

    def accept(self, visitor: ExprVisitor):
        return visitor.visitBinaryExpr(self)


@dataclass
class UnaryExpr(Expr):
    expr: Expr
    operator: Token

    def accept(self, visitor: ExprVisitor):
        return visitor.visitUnaryExpr(self)


@dataclass
class GroupingExpr(Expr):
    expr: Expr

    def accept(self, visitor: ExprVisitor):
        return visitor.visitGroupingExpr(self)


@dataclass
class LiteralExpr(Expr):
    number: float

    def accept(self, visitor: ExprVisitor):
        return visitor.visitLiteralExpr(self)
