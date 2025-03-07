from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A can be a Knight or a Knave
    Or(AKnight, AKnave),

    # A can't be a Knight and a Knave
    Not(And(AKnight, AKnave)),

    # If A is a Knight then A is a Knave
    Implication(AKnight, AKnave),

    # If A is a Knave then A is neither a Knight nor a Knave
    Implication(AKnave, Not(And(AKnight, AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A can be a Knight or a Knave
    Or(AKnight, AKnave),
    
    # B can be a Knight or a Knave
    Or(BKnight, BKnave),

    # A can't be a Knight and a Knave
    Not(And(AKnight, AKnave)),
    
    # A can't be a Knight and a Knave
    Not(And(BKnight, BKnave)),

    # If A is a Knight then A and B are Knaves
    Implication(AKnight, And(AKnave, BKnave)),

    # If A is a Knave then A and B aren't Knaves
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A can be a Knight or a Knave
    Or(AKnight, AKnave), 

    # B can be a Knight or a Knave
    Or(BKnight, BKnave),

    # A can't be a Knight and a Knave
    Not(And(AKnight, AKnave)),

    # B can't be a Knight and a Knave
    Not(And(BKnight, BKnave)),

    # If A is a Knight then A and B are either both knights or both knaves 
    Implication(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # If A is a Knave then A and B are different kinds
    Implication(AKnave, Or(And(AKnight, BKnave), And(AKnave, BKnight))),

    # If B is a Knight then A and B are different kinds
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))),
    
    # If B is a Knave then A and B are either both knights or both knaves 
    Implication(BKnave, Or(And(AKnight, BKnight), And(AKnave, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A can be a Knight or a Knave
    Or(AKnight, AKnave), 

    # B can be a Knight or a Knave
    Or(BKnight, BKnave),

    # C can be a Knight or a Knave
    Or(CKnight, CKnave),

    # A can't be a Knight and a Knave
    Not(And(AKnight, AKnave)),

    # B can't be a Knight and a Knave
    Not(And(BKnight, BKnave)),

    # C can't be a Knight and a Knave
    Not(And(BKnight, BKnave)),

    # If B is Knight and A is a Knight then A is a Knave
    Implication(BKnight, Implication(AKnight, AKnave)),

    # If B is a Knight and A is a Knave then A is a Knight
    Implication(BKnight, Implication(AKnave, AKnight)),

    # If B is a Knight then C is a Knave.
    Implication(BKnight, CKnave),

    # If B is a Knave then C is a Knight
    Implication(BKnave, CKnight),

    # If C is a Knight then A is a Knight
    Implication(CKnight, AKnight),

    # If C is a Knave then A is a Knave 
    Implication(CKnave, AKnave)
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
