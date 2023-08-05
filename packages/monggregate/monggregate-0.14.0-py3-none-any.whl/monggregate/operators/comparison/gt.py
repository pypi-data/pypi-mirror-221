"""
Module defining an interface to MongoDB $gt operator

Online MongoDB documentation:
--------------------------------------------------------------------------------------------------------------------
Last Updated (in this package) : 19/11/2022
Source : https://www.mongodb.com/docs/manual/reference/operator/aggregation/gt/#mongodb-expression-exp.-gt

Definition
--------------------
$gt
Compares two values and returns:

    * true when the first value is greater than the second value.

    * false when the first value is less than or equivalent to the second value.

The $gt compares both value and type, using the specified BSON comparison order for values of different types.

$gt has the following syntax:

    >>> { $gt: [ <expression1>, <expression2> ] }

For more information on expressions, see Expressions.
"""

from typing import Any
from monggregate.operators.comparison.comparator import Comparator

class GreatherThan(Comparator):
    """
    Creates a $gt expression

    Attributes
    -------------------
        - left, Expression : Left operand. Can be any valid expression.
        - right, Expression : Right operand. Can be any valid expression.

    """

    @property
    def statement(self) -> dict:

        return self.resolve({
            "$gt":[self.left, self.right]
        })

Gt = GreatherThan

def greather_than(left:Any, right:Any)->dict:
    """Returns a $gt statement"""

    return GreatherThan(
        left = left,
        right = right
        ).statement

gt= greather_than