# Draco Rules:

## Declarations

- **Signed:** `signed 100 temp;`
- **Unsigned:** `unsigned 100 temp;`
- **Enum:** `enum {c_red, c_yellow, c_blue, c_black, c_white}`
- **Pointer Types:** `*int`
- **Array Types:** `[MAX_NAME_LENGTH + 1] char` `[M, N, P] int` `[BLOCK_COUNT] [BLOCK_LEN] unsigned 32`
- **Struct:** `ProcessQueue_t = struct {
			*ProcessQueue_t pq_next;
			*Process_t pq_this;
		    };`
- **Union:** `type
		    Track_t = union {
			int tr_straight;	/* straight track option */
			struct {		/* turnout option */
			    int trn_length;
			    bool trn_open;
			    bool trn_isRight;
			} tr_turnout;
		    };`
- **procedure:** `proc (int a, b)int`

#### The following types are supplied predefined:
**int** - signed numeric using the standard fully supported word
**size** on the host processor 
**short** - smaller sized signed value (often 8 bit)
**word** - unsigned numeric, same size as int
**ushort** - unsigned numeric, same size as short
**byte** - unsigned numeric, one byte long (8 bits)
**char** - enumeration type of all 256 character values
**bool** - enumeration type consisting of 'false' and 'true'

## Procedures

Procedures start with `proc` and terminate with `corp`.

*procedure example:*

```draco
proc minimum([*] int a)int:
    int i, min;

    min := a[0];
    for i from 1 upto dim(a, 1) - 1 do
    if a[i] < min then
        min := a[i];
    fi;
    od;
    min
corp;
```

## Statements

- **Assignment:** `a := b;`
- **Procedure Call:** `example(a);`
- **If-elif-else:** `if a < b then a := b; elif a > b then a := b; else a := b; fi;` *(**fi** is used if there is no else)*
- **While:** `while a < b do a := b; od;` *(go check docs for a weird example)*
- **For:** `for i from 0 upto 10 do a := b; od;` *(**downto** is also available)*
- **Case:** ```case ch
	    incase 'a':
	    incase 'A':
		writeln("It was an A.");
	    incase 'b' .. 'd':
	    incase 'B' .. 'D':
		x := y;
		y := z;
	    default:
		flag := true;
	    esac;```
- **free:** `free a;` (not sure if correct)
- **pretend:** pretend(expr, type);
- **error:** ```if range(IDENTIFIER) > 255 then
		error("IDENTIFIER range must be <= 255");
	    fi;```

## Expressions

- **\*** dereferencing operator.
- **&** prefix address-of operator.
----------------

- **[]** postfix array indexing operator.
- **.** field selection.
- **()** function calling.
----------------
- **~** prefix bitwise complement operator.
- **&** bitwise and opertor.
- **><** bitwise exclusive-or operator.
- **<<** logical left shit operator.
- **>>** logical right shift operator.
- **|** bitwise inclusive-or operator.
----------------
- **|** prefix numeric absolute value operator.
- **-** prefix numeric negation operator.
- **+** prefix numeric do-nothing operator.
----------------
- **\*** multiplcation operator.
- **/** division operator.
- **%** remainder operator.
- **+** addition operator.
- **-** subtraction operator.
----------------
- **>, <, >=, <=, =, ~=** comparison operators.
----------------
- **and, or, not** boolean operations.
----------------
- **dim**(arrayname, number)
- **sizeof**(type)
- **new**(type)
- **range**(type)

## Basic components of Draco programs

- **Identifiers can be any length.**
- **Comments** are of the format `/*` `*/` and can be nested.
- **Numeric Constants** can be in decimal(d), octal(o), hexadecimal(x) or binary(b) for example: 0b1010. Hexadecimal digits can be given in uppercase or lowercase.
- **'** delimit single characters.
- **"** delimit strings.

**Escape Characters:**
- \b - the ASCII backspace character
- \t - the ASCII tab character
- \r - the ASCII carriage return character
- \n - the ASCII linefeed (newline) character
- \e - the C - style string termination character (0)

**Alternate Forms:**

    standard	 alternate
	    \		    #
	    [		    (:
	    ]		    :)
	    {		    ($
	    }		    $)
	    ~=		    /=
	    ~		    $-
	    |		    $/
	    _		    ^

```draco
type type1 = struct {int field1, field2; char field3};
type type2 = [2] type1;
type2 CONST = ((1, 2, 'a'), (3, 4, 'a' - FRED / 2));
type2 var;
...
var := type2((-26, 13 + 2 / 7, 'a' + 2), (+1, -1, '\e'));
```

## Draco I/O system

**write example:**
```draco
i : 123
j : 12
n : 60528
w : 0xabc

write(i, n : u, ' ', w:x:-4, i:j)
```

**read example**
```draco
proc main()void:
    int n, sum, i;

    sum := 0;
    write('>');
    for i from 1 upto 10 do
    while
        if read(n) then
        /* got a number! */
        false
        else
        case ioerror()
        incase CH_EOF:
            writeln("*** You're not done yet! ***");
        incase CH_MISSING:
            /* nothing left on this line */
            ;
        default:
            writeln("*** Invalid number - keep going. ***");
        esac;
        write('>');
        readln();
        true
        fi
    do
    od;
    sum := sum + n;
    od;
    writeln("Sum = ", sum);
corp;
```

## Operator Types

```
type Complex_t = ("_cmplx", struct {int c_real, c_imag},
            OPADD | OPSUB | OPMUL | OPDIV | OPNEG |
            OPABS | OPCPR | OPPUT | OPGET);
Complex_t I = (0, 1);
```

The various names for the include files:
```draco
OPADD - the binary '+' operator
OPSUB - the binary '-' operator
OPMUL - the binary '*' operator
OPDIV - the binary '/' operator
OPMOD - the binary '%' operator
OPNEG - the unary '-' operator
OPABS - the unary '|' operator
OPIOR - the binary '|' operator
OPAND - the binary '&' operator
OPXOR - the binary '><' operator
OPSHL - the binary '<<' operator
OPSHR - the binary '>>' operator
OPNOT - the unary '~' operator
OPCPR - the binary comparison operators
OPPUT - text output using 'write' and 'writeln'
OPGET - text input using 'read' and 'readln'
```