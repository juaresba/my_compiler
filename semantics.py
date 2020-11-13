from non_terminals import NonTerminal
from rules_semantics import RuleS
from scope import Object, ScopeAnalyser, Kind, intObj, boolObj, charObj, stringObj, universalObj, Alias, Array, Struct, Function, Var, Field, Param, Type
from types import Attribute, functionVarPos, curFunction, IDDStatic, IDUStatic, IDStatic, TStatic, LIStatic, LI0Static, LI1Static, TRUStatic, FALSStatic, STRStatic, CHRStatic, NUMStatic, DCStatic, DC0Static, DC1Static, LPStatic, LP0Static, LP1Static, EStatic, E0Static, E1Static, LStatic, L0Static, L1Static, RStatic, R0Static, R1Static, YStatic, Y0Static, Y1Static, FStatic, F0Static, F1Static, LVStatic, LV0Static, LV1Static, MCStatic, LEStatic, LE0Static, LE1Static, MTStatic, MEStatic, MWStatic, NBStatic

class Analyser:
	def __init__(self, lexical_anl):
		self.stack = []
		self.lexical_analyser = lexical_anl
		self.scope = ScopeAnalyser()
		self.output_file = open("output_code", "w")
		self.nfuncs = 0
		self.label = 0

	def pop(self):
		self.stack.pop()

	def push(self, attr):
		self.stack.append(attr)

	def top(self):
		if len(self.stack) == 0:
			return Attribute()
		
		return self.stack[-1]
	
	def parse(self, rule):
		if RuleS.P0:
			pass

		elif RuleS.LDE0:
			pass

		elif RuleS.LDE1:
			pass

		elif RuleS.DE0:
			pass

		elif RuleS.DE1:
			pass

		elif RuleS.T0: # T-> 'integer'
			t = TStatic.attribute
			t.type = intObj

			TStatic.size = 1
			TStatic.type = NonTerminal.T
			TStatic.attribute = t

			self.push(TStatic)
			pass

		elif RuleS.T1: # T -> 'char'
			t = TStatic.attribute
			t.type = charObj

			TStatic.size = 1
			TStatic.type = NonTerminal.T
			TStatic.attribute = t

			self.push(TStatic)
			pass

		elif RuleS.T2: # T -> 'boolean'
			t = TStatic.attribute
			t.type = boolObj

			TStatic.size = 1
			TStatic.type = NonTerminal.T
			TStatic.attribute = t

			self.push(TStatic)
			pass

		elif RuleS.T3: # T -> 'string'
			t = TStatic.attribute
			t.type = stringObj

			TStatic.size = 1
			TStatic.type = NonTerminal.T
			TStatic.attribute = t

			self.push(TStatic)
			pass

		elif RuleS.T4: # T -> IDU
			IDUStatic = self.top()
			id = IDUStatic.attribute
			p = id.Object
			self.pop()

			if p.kind.IsType() or p.kind == Kind.KindUniversal:
				t = TStatic.attribute
				t.type = p
				TStatic.attribute = t

				if p.kind == Kind.KindAliasType:
					alias = p.T
					TStatic.size = alias.size
				elif p.kind == Kind.KindArrayType:
					arr = p.T
					TStatic.size = arr.size
				elif p.kind == Kind.KindStructType:
					strct = p.T
					TStatic.size = strct.size
				
			else:
				t = TStatic.attribute
				t.type = universalObj

				TStatic.attribute = t
				TStatic.size = 0
			
			TStatic.type = NonTerminal.T
			self.push(TStatic)
			pass

		elif RuleS.DT0: # DT -> 'type' IDD '=' 'array' '[' NUM ']' 'of' T
			TStatic = self.top()
			self.pop()
			NUMStatic = self.top()
			self.pop()
			IDDStatic = self.top()
			self.pop()

			id = IDDStatic.attribute
			num = NUMStatic.attribute
			typ = TStatic.attribute

			p = id.Object
			n = num.Val
			t = typ.type

			p.kind = Kind.KindArrayType
			p.T = Array()
			p.T.num_elements = n
			p.T.elem_type = t
			p.t.size = n
			
			pass

		elif RuleS.DT1: # DT -> 'type' IDD '=' 'struct' NB '{' DC ''
			DCStatic = self.top()
			self.pop()
			IDDStatic = self.top()
			self.pop()

			obj = IDDStatic.attribute
			dc = DCStatic.attribute
			p = obj.Object

			p.kind = Kind.KindStructType
			p.T = Struct
			p.T.fields = dc.list
			p.T.size = DCStatic.size
			
			self.scope.end_block()
			pass

		elif RuleS.DT2: # DT -> 'type' IDD '=' T
			TStatic = self.top()
			self.pop()
			IDDStatic = self.top()
			self.pop()

			id = IDDStatic.attribute
			typ = TStatic.attribute

			p = id.Object
			t = typ.type

			p.kind = Kind.KindAliasType
			p.T = Alias
			p.T.base_type = t
			p.T.size = TStatic.size
			
			pass

		elif RuleS.DC0: # DC -> DC ';' LI ':' T
			TStatic = self.top()
			self.pop()
			LIStatic = self.top()
			self.pop()
			DC1Static = self.top()
			self.pop()

			li = LIStatic.attribute
			typ = TStatic.attribute

			p = li.List
			t = typ.type
			n = DC1Static.size

			while p is not None and p.kind == Kind.KindUndefined:

				p.kind = Kind.KindField

				if p.T is not None:
					field = p.T
				else:
					field = Field()
					field.pype = t
					field.index = n
					field.size = TStatic.size
				
				p.T = field

				n = n + TStatic.size
				p = p.Next
			

			dc0 = DC0Static.attribute
			dc1 = DC1Static.attribute
			dc0.List = dc1.List
			DC0Static.size = n
			DC0Static.type = NonTerminal.DC

			self.push(DC0Static)
			pass

		elif RuleS.DC1: # DC -> LI ':' T
			TStatic = self.top()
			self.pop()
			LIStatic = self.top()
			self.pop()

			li = LIStatic.attribute
			p = li.List
			ts = TStatic.attribute
			t = ts.type
			n = 0

			while True:
				if p is None or p.kind != Kind.KindUndefined:
					pass

				p.kind = Kind.KindField
				
				if p.T is not None:
					field = p.T
				else:
					field = Field()
					field.pype = t
					field.index = n
					field.size = TStatic.size
				
				p.T = field

				n = n + TStatic.size
				p = p.Next
			

			dc = DCStatic.attribute
			li = LIStatic.attribute
			dc.List = li.List
			DCStatic.attribute = dc

			self.push(DCStatic)
			pass

		elif RuleS.DF0: # DF -> 'function' IDD NF '(' LP ')' ':' T MF B
			self.scope.end_block()
			pass

		elif RuleS.LP0: # LP -> LP ',' IDD ':' T
			TStatic = self.top()
			self.pop()
			IDDStatic = self.top()
			self.pop()
			LP1Static = self.top()
			self.pop()

			id = IDDStatic.attribute
			typ = TStatic.attribute

			p = id.Object
			t = typ.type
			n = LP1Static.size

			p.kind = Kind.KindParam
			p.T = Param()
			p.T.ptype = t
			p.T.index =	n
			p.T.size = TStatic.size
			

			lp1 = LP1Static.attribute
			lp0 = LP0Static.attribute
			lp0.List = lp1.List
			LP0Static.attribute = lp0
			LP0Static.size = n + TStatic.size
			LP0Static.type = NonTerminal.LP
			self.push(LP0Static)
			pass

		elif RuleS.LP1: # LP -> IDD ':' T
			TStatic = self.top()
			self.pop()
			IDDStatic = self.top()
			self.pop()

			id = IDDStatic.attribute
			typ = TStatic.attribute

			p = id.Object
			t = typ.type

			p.kind = Kind.KindParam
			if param is not None:
				param = p.T 
			else:
				param = Param()
				param.ptype = t
				param.index = 0
				param.size = TStatic.size
			
			p.T = param

			lp = LPStatic.attribute
			lp.List = p
			LPStatic.attribute = lp
			LPStatic.size = TStatic.size
			LPStatic.type = NonTerminal.LP

			self.push(LPStatic)
			pass

		elif RuleS.B0: # B -> '{' LDV LS ''

			#self.output_file.write("END_FUNC\n")
			#pos, _ = self.output_file.seek
			#self.output_file.seek
			#funct = f.T
			#self.output_file.write("%02d", funct.Vars)
			#self.output_file.seek
			pass


		elif RuleS.LDV0: # LDV -> LDV DV
			pass
		elif RuleS.LDV1: # LDV -> DV
			pass
		elif RuleS.LS0: # LS -> LS S
			pass
		elif RuleS.LS1: # LS -> S
			pass

		elif RuleS.DV0: # DV -> 'var' LI ':' T ';'
			TStatic = self.top()
			typ = TStatic.attribute
			t = typ.type
			self.pop()

			LIStatic = self.top()
			self.pop()

			li = LIStatic.attribute
			p = li.List
			funct = curFunction.T
			n = funct.Params

			while p is not None and p.kind == Kind.KindUndefined:

				p.kind = Kind.KindVar
				
				if p.T is not None:
					v = p.T
				else:
					v = Var()
					v.ptype = t
					v.size = TStatic.size
					v.index = n					
				
				p.T = v

				n = n + TStatic.size
				p = p.Next
			

			funct = curFunction.T
			funct.Vars = n
			curFunction.T = funct
			pass

		elif RuleS.LI0: # LI -> LI ',' IDD
			IDDStatic = self.top()
			self.pop()
			LI1Static = self.top()
			self.pop()

			li0 = LI0Static.attribute
			li1 = LI0Static.attribute
			li0.List = li1.List
			LI0Static.type = NonTerminal.LI
			LI0Static.attribute = li0
			self.push(LI0Static)
			pass

		elif RuleS.LI1: # LI -> IDD
			IDDStatic = self.top()
			self.pop()

			li = LIStatic.attribute
			li.List = IDDStatic.attribute.Object
			LIStatic.attribute = li
			LIStatic.type = NonTerminal.LI
			self.push(LIStatic)
			pass

		elif RuleS.S0: # S -> M
			pass

		elif RuleS.S1: # S -> U
			pass

		elif RuleS.U0: # U -> 'if' '(' E ')' MT S
			MTStatic = self.top()
			self.pop()
			EStatic = self.top()
			self.pop()

			e = EStatic.attribute
			t = e.type

			mt = MTStatic.attribute
			self.output_file.write("L%d\n", mt.Label)
			pass

		elif RuleS.U1: # U -> 'if' '(' E ')' MT M 'else' ME U
			MEStatic = self.top()
			self.pop()
			MTStatic = self.top()
			self.pop()
			EStatic = self.top()
			self.pop()

			me = MEStatic.attribute
			e = MEStatic.attribute

			l = me.Label
			t = e.type

			self.output_file.write("L%d", l)
		elif RuleS.M0: # M -> 'if' '(' E ')' MT M 'else' ME M
			MEStatic = self.top()
			self.pop()
			MTStatic = self.top()
			self.pop()
			EStatic = self.top()
			self.pop()

			me = MEStatic.attribute
			e = MEStatic.attribute

			l = me.Label
			t = e.type

			self.output_file.write("L%d", l)
			pass

		elif RuleS.M1: # M -> 'while' MW '(' E ')' MT M
			MTStatic = self.top()
			self.pop()
			EStatic = self.top()
			self.pop()
			MWStatic = self.top()
			self.pop()

			mw = MWStatic.attribute
			mt = MTStatic.attribute
			es = EStatic.attribute

			l1 = mw.Label
			l2 = mt.Label

			t = es.type

			self.output_file.write("\tTJMP_BW L%d\nL%d\n", l1, l2)
			pass

		elif RuleS.M2: # M -> 'do' MW M 'while' '(' E ')' ';'
			EStatic = self.top()
			self.pop()
			MWStatic = self.top()
			self.pop()

			mw = MWStatic.attribute
			es = EStatic.attribute

			l = mw.Label
			t = es.type

			self.output_file.write("\tNOT\n\tTJMP_BW L%d\n", l)
			pass

		elif RuleS.M3: # M -> NB B
			self.scope.end_block()
			pass

		elif RuleS.M4: # M -> LV '=' E ';'
			EStatic = self.top()
			self.pop()
			LVStatic = self.top()
			self.pop()

			lv = LVStatic.attribute

			t = lv.type
			typ = lv.type.T

			self.output_file.write("\tSTORE_REF %d\n", typ.size)
			pass


		elif RuleS.M5: # M -> 'pass' ';'
			pass
		elif RuleS.M6: # M -> 'continue' ';'
			pass

		elif RuleS.E0: # E -> E 'and' L
			LStatic = self.top()
			self.pop()
			E1Static = self.top()
			self.pop()

			e = E0Static.attribute
			e.type = boolObj
			E0Static.attribute = e

			self.push(E0Static)

			self.output_file.write("\tAND\n")
			pass

		elif RuleS.E1: # E -> E 'or' L
			LStatic = self.top()
			self.pop()
			E1Static = self.top()
			self.pop()

			e = E0Static.attribute
			e.type = boolObj
			E0Static.attribute = e

			self.push(E0Static)

			self.output_file.write("\tOR\n")
			pass

		elif RuleS.E2: # E -> L
			LStatic = self.top()
			self.pop()

			e = EStatic.attribute
			l = LStatic.attribute
			e.type = l.type

			EStatic.attribute = e
			EStatic.type = NonTerminal.E

			self.push(EStatic)
			pass

		elif RuleS.L0: # L -> L '<' R
			RStatic = self.top()
			self.pop()
			L1Static = self.top()
			self.pop()

			l = L0Static.attribute
			l.type = boolObj
			L0Static.attribute = l
			L0Static.type = NonTerminal.L

			self.push(L0Static)
			self.output_file.write("\tLT\n")
			pass

		elif RuleS.L1: # L -> L '>' R
			RStatic = self.top()
			self.pop()
			L1Static = self.top()
			self.pop()

			l = L0Static.attribute
			l.type = boolObj
			L0Static.attribute = l
			L0Static.type = NonTerminal.L

			self.push(L0Static)
			self.output_file.write("\tGT\n")
			pass

		elif RuleS.L2: # L -> L '<=' R
			RStatic = self.top()
			self.pop()
			L1Static = self.top()
			self.pop()

			l = L0Static.attribute
			l.type = boolObj
			L0Static.attribute = l
			L0Static.type = NonTerminal.L

			self.push(L0Static)
			self.output_file.write("\tLE\n")
			pass

		elif RuleS.L3: # L -> L '>=' R
			RStatic = self.top()
			self.pop()
			L1Static = self.top()
			self.pop()

			l = L0Static.attribute
			l.type = boolObj
			L0Static.attribute = l
			L0Static.type = NonTerminal.L

			self.push(L0Static)
			self.output_file.write("\tGE\n")
			pass

		elif RuleS.L4: # L -> L '==' R
			RStatic = self.top()
			self.pop()
			L1Static = self.top()
			self.pop()

			l = L0Static.attribute
			l.type = boolObj
			L0Static.attribute = l
			L0Static.type = NonTerminal.L

			self.push(L0Static)
			self.output_file.write("\tEQ\n")
			pass

		elif RuleS.L5: # L -> L '!=' R
			RStatic = self.top()
			self.pop()
			L1Static = self.top()
			self.pop()

			l = L0Static.attribute
			l.type = boolObj
			L0Static.attribute = l
			L0Static.type = NonTerminal.L

			self.push(L0Static)
			self.output_file.write("\tNE\n")
			pass

		elif RuleS.L6: # L -> R
			RStatic = self.top()
			self.pop()

			ls = LStatic.attribute
			rs = RStatic.attribute

			ls.type = rs.type
			LStatic.attribute = ls
			LStatic.type = NonTerminal.L

			self.push(LStatic)
			pass

		elif RuleS.R0: # R -> R '+' Y
			YStatic = self.top()
			self.pop()
			R1Static = self.top()
			self.pop()

			r0 = R0Static.attribute
			r1 = R1Static.attribute
			r0.type = r1.type

			R0Static.attribute = r0
			R0Static.type = NonTerminal.R

			self.push(R0Static)
			self.output_file.write("\tADD\n")
			pass

		elif RuleS.R1: # R -> R '-' Y
			YStatic = self.top()
			self.pop()
			R1Static = self.top()
			self.pop()

			r0 = R0Static.attribute
			r1 = R1Static.attribute
			r0.type = r1.type

			R0Static.attribute = r0
			R0Static.type = NonTerminal.R

			self.push(R0Static)
			self.output_file.write("\tSUB\n")
			pass

		elif RuleS.R2: # R -> Y
			YStatic = self.top()
			self.pop()
			r = RStatic.attribute
			y = YStatic.attribute
			r.type = y.type

			RStatic.attribute = r
			RStatic.type = NonTerminal.R

			self.push(RStatic)
			pass

		elif RuleS.Y0: # Y -> Y '*' F
			FStatic = self.top()
			self.pop()
			Y1Static = self.top()
			self.pop()

			y0 = Y0Static.attribute
			y1 = Y1Static.attribute
			y0.type = y1.type

			Y0Static.attribute = y0
			Y0Static.type = NonTerminal.Y
			self.push(Y0Static)

			self.output_file.write("\tMUL\n")
			pass

		elif RuleS.Y1: # Y -> Y '/' F
			FStatic = self.top()
			self.pop()
			Y1Static = self.top()
			self.pop()

			y0 = Y0Static.attribute
			y1 = Y1Static.attribute
			y0.type = y1.type

			Y0Static.attribute = y0
			Y0Static.type = NonTerminal.Y
			self.push(Y0Static)

			self.output_file.write("\tDIV\n")
			pass

		elif RuleS.Y2: # Y -> F
			FStatic = self.top()
			self.pop()

			y = YStatic.attribute
			f = FStatic.attribute
			y.type = f.type
			Y0Static.attribute = y
			Y0Static.type = NonTerminal.Y

			self.push(Y0Static)
			pass

		elif RuleS.F0: # F -> LV
			LVStatic = self.top()
			self.pop()

			lv = LVStatic.attribute
			typ = lv.type.T

			n = typ.size

			f = FStatic.attribute
			f.type = lv.type
			FStatic.attribute = f
			FStatic.type = NonTerminal.F

			self.push(FStatic)
			self.output_file.write("\tDE_REF %d\n", n)
			pass

		elif RuleS.F1: # F -> ' += 1' LV
			LVStatic = self.top()
			self.pop()

			lv = LVStatic.attribute
			t = lv.type

			fs = FStatic.attribute
			fs.type = intObj
			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)
			self.output_file.write("\tDUP\n\tDUP\n\tDE_REF 1\n")
			self.output_file.write("\tINC\n\tSTORE_REF 1\n\tDE_REF 1\n")
			pass

		elif RuleS.F2: # F -> '--' LV
			LVStatic = self.top()
			self.pop()

			lv = LVStatic.attribute
			t = lv.type

			fs = FStatic.attribute
			fs.type = lv.type
			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)
			self.output_file.write("\tDUP\n\tDUP\n\tDE_REF 1\n")
			self.output_file.write("\tINC\n\tSTORE_REF 1\n\tDE_REF 1\n")
			pass

		elif RuleS.F3: # F -> LV ' += 1'
			LVStatic = self.top()
			self.pop()

			lv = LVStatic.attribute
			t = lv.type

			fs = FStatic.attribute
			fs.type = lv.type
			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)
			self.output_file.write("\tDUP\n\tDUP\n\tDE_REF 1\n")
			self.output_file.write("\tINC\n\tSTORE_REF 1\n\tDE_REF 1\n")
			self.output_file.write("\tDEC\n")
			pass

		elif RuleS.F4: # F -> LV '--'
			LVStatic = self.top()
			self.pop()

			lv = LVStatic.attribute
			t = lv.type

			fs = FStatic.attribute
			fs.type = t
			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)
			self.output_file.write("\tDUP\n\tDUP\n\tDE_REF 1\n")
			self.output_file.write("\tDEC\n\tSTORE_REF 1\n\tDE_REF 1\n")
			self.output_file.write("\tINC\n")
			pass

		elif RuleS.F5: # F -> '(' E ')'
			EStatic = self.top()
			self.pop()

			fs = FStatic.attribute
			es = EStatic.attribute
			fs.type = es.type
			FStatic.attribute = fs

			self.push(FStatic)
			pass

		elif RuleS.F6: # F -> IDU MC '(' LE ')'
			LEStatic = self.top()
			self.pop()
			MCStatic = self.top()
			self.pop()
			IDUStatic = self.top()
			self.pop()

			id = IDUStatic.attribute
			f = id.Object

			fs = FStatic.attribute
			ms = MCStatic.attribute
			fs.type = ms.type
			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)

			funct = f.T
			self.output_file.write("\tCALL %d\n", funct.Index)
			pass

		elif RuleS.F7: # F -> '-' F
			F1Static = self.top()
			self.pop()

			f1 = F1Static.attribute
			t = f1.type

			f0 = F0Static.attribute
			f0.type = t
			F0Static.attribute = f0
			F0Static.type = NonTerminal.F

			self.push(F0Static)
			self.output_file.write("\tNEG\n")
			pass

		elif RuleS.F8: # F -> '!' F
			F1Static = self.top()
			self.pop()

			f1 = F1Static.attribute
			t = f1.type

			f0 = F0Static.attribute
			f0.type = t
			F0Static.attribute = f0
			F0Static.type = NonTerminal.F

			self.push(F0Static)
			self.output_file.write("\tNOT\n")
			pass

		elif RuleS.F9: # F -> TRUE
			TRUStatic = self.top()
			self.pop()

			fs = FStatic.attribute
			fs.type = boolObj
			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)

			self.output_file.write("\tLOAD_CONST %d\n", self.lexical_analyser.SecondaryToken)
			pass

		elif RuleS.F10: # F -> FALSE
			FALSStatic = self.top()
			self.pop()

			fs = FStatic.attribute
			fs.type = boolObj

			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)

			self.output_file.write("\tLOAD_CONST %d\n", self.lexical_analyser.SecondaryToken)
			pass

		elif RuleS.F11: # F -> CHR
			CHRStatic = self.top()
			self.pop()

			fs = FStatic.attribute
			fs.type = charObj

			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)

			n = self.lexical_analyser.SecondaryToken
			self.output_file.write("\tLOAD_CONST %d\n", n)
			pass

		elif RuleS.F12: # F -> STR
			STRStatic = self.top()
			self.pop()

			fs = FStatic.attribute
			fs.type = stringObj

			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)

			n = self.lexical_analyser.SecondaryToken
			self.output_file.write("\tLOAD_CONST %d\n", n)
			pass

		elif RuleS.F13: # F -> NUM
			NUMStatic = self.top()
			self.pop()

			fs = FStatic.attribute
			fs.type = intObj

			FStatic.attribute = fs
			FStatic.type = NonTerminal.F

			self.push(FStatic)

			n = self.lexical_analyser.SecondaryToken
			self.output_file.write("\tLOAD_CONST %d\n", n)
			pass

		elif RuleS.LE0: # LE -> LE ',' E
			EStatic = self.top()
			self.pop()
			LE1Static = self.top()
			self.pop()

			le0 = LE0Static.attribute
			le1 = LE1Static.attribute
			le0.Param = None
			le0.Err = le1.Err
			LE0Static.attribute = le0

			n = le1.N
			if le1.Err != 0:
				p = le1.Param
				if p is None:
					le0 = LE0Static.attribute
					le0.Err = 1
					LE0Static.attribute = le0
				else:
					le0 = LE0Static.attribute
					le0.Param = p.Next
					le0.N = n + 1
					LE0Static.attribute = le0
				
			

			LE0Static.type = NonTerminal.LE
			self.push(LE0Static)
			pass

		elif RuleS.LE1: # LE -> E
			EStatic = self.top()
			self.pop()
			MCStatic = self.top()

			le = LEStatic.attribute
			mc = MCStatic.attribute
			le.Param = None
			le.Err = mc.Err
			LEStatic.attribute = le
			n = 1

			if mc.Err != 0:
				p = mc.Param
				if p is None:
					le = LEStatic.attribute
					le.Err = 1
					LEStatic.attribute = le
				else:
					le = LEStatic.attribute
					le.Param = p.Next
					le.N = n + 1
					LEStatic.attribute = le
				
			

			LEStatic.type = NonTerminal.LE
			self.push(LEStatic)
		elif RuleS.LV0: # LV -> LV '.' IDU
			IDStatic = self.top()
			self.pop()
			LV1Static = self.top()
			self.pop()

			lv1 = LV1Static.attribute
			t = lv1.type

			if t.kind != Kind.KindStructType:
				if t.kind != Kind.KindUniversal:
					# todo
					pass
				
				lv0 = LV0Static.attribute
				lv0.type = universalObj
				LV0Static.attribute = lv0
			else:
				st = t.T
				p = st.Fields

				while p is not None:
					ids = IDStatic.attribute
					if p.name == ids.name:
						pass

					
					p = p.Next
				

				if p is None:
					lv0 = LV0Static.attribute
					lv0.type = universalObj
					LV0Static.attribute = lv0
				else:
					lv0 = LV0Static.attribute
					field = p.T
					lv0.type = field.ptype

					typ = lv0.type.T
					typ.size = field.size
					lv0.type.T = typ

					LV0Static.attribute = lv0

					self.output_file.write("\tADD %d", field.Index)
				
			

			LV0Static.type = NonTerminal.LV
			self.push(LV0Static)
			pass

		elif RuleS.LV1: # LV -> LV '[' E ']'
			EStatic = self.top()
			self.pop()
			LV1Static = self.top()
			self.pop()

			t = LV1Static.attribute.type

			lv0 = LV0Static.attribute
			if self.scope.check_types(t, stringObj):
				lv0.type = charObj
			elif t.kind == Kind.KindArrayType:
				if t.kind == Kind.KindUniversal:
					# err
					pass
				
				lv0.type = universalObj
			else:
				elemType = t.T.elem_type
				lv0.type = elemType
				n = elemType.T.size

				self.output_file.write("\tMUL %d\n\tADD\n", n)
			

			# if self.scope.CheckTypes(EStatic.attribute.type, intObj)

			LV0Static.type = NonTerminal.LV
			LV0Static.attribute = lv0
			pass

		elif RuleS.LV2: # LV -> IDU
			IDUStatic = self.top()
			self.pop()

			p = IDUStatic.attribute.Object
			lv = LVStatic.attribute
			
			if p.T is not None:
				vart = p.T 
			else: 
				vart = Var()
				vart.ptype = Object
			
			if p.kind != Kind.KindVar and p.kind != Kind.KindParam:
				if p.kind != Kind.KindUniversal:
					# err
					pass
				
				lv.type = universalObj
			else:
				lv.type = vart.ptype

				if lv.type.T is not None:
					typ = lv.type.T 
				else:
					typ = Type()
					typ.size = vart.size

				if p.kind == Kind.KindParam:
					typ.size = p.T.size
				

				lv.type.T = typ
				self.output_file.write("\tLOAD_REF %d\n", vart.Index)
			
			LVStatic.attribute = lv
			LVStatic.type = NonTerminal.LV

			t = lv.type

			self.push(LVStatic)
			pass

		elif RuleS.IDD0: # IDD -> Id
			name = self.lexical_analyser.SecondaryToken
			ids = IDDStatic.attribute
			ids.name = name

			p = self.scope.search_local_symbol(name)
			if p is not None:
				# err
				pass
			else:
				p = self.scope.define_symbol(name)
			

			ids.Object = p
			IDDStatic.attribute = ids

			self.push(IDDStatic)
			pass

		elif RuleS.IDU0: # IDU -> Id
			name = self.lexical_analyser.SecondaryToken
			idu = IDUStatic.attribute
			idu.name = name
			p = self.scope.search_global_symbol(name)
			
			if p is None:
				# err ?
				p = self.scope.define_symbol(name)
			

			idu.Object = p
			IDUStatic.attribute = idu

			self.push(IDUStatic)
			pass

		elif RuleS.ID0: # ID -> Id
			name = self.lexical_analyser.SecondaryToken
			ids = IDStatic.attribute
			ids.name = name
			ids.Object = None
			IDDStatic.attribute = ids
			self.push(IDDStatic)
			pass

		elif RuleS.TRUE0: # TRUE ->  'true'
			tru = TRUStatic.attribute
			tru.type = boolObj
			tru.Val = 1

			TRUStatic.type = NonTerminal.TRUE
			TRUStatic.attribute = tru

			self.push(TRUStatic)
			pass

		elif RuleS.FALSE0: # FALSE -> 'false'
			fals = TRUStatic.attribute
			fals.type = boolObj
			fals.Val = 0

			FALSStatic.type = NonTerminal.FALSE
			FALSStatic.attribute = fals

			self.push(FALSStatic)
			pass

		elif RuleS.CHR0: # CHR -> c
			chr = CHRStatic.attribute
			chr.type = charObj
			chr.Pos = self.lexical_analyser.SecondaryToken
			chr.Val = self.lexical_analyser.GetRuneConstant(self.lexical_analyser.SecondaryToken)

			CHRStatic.type = NonTerminal.CHR
			CHRStatic.attribute = chr

			self.push(CHRStatic)
			pass

		elif RuleS.STR0: # STR -> s
			str = STRStatic.attribute
			str.type = stringObj
			str.Pos = self.lexical_analyser.SecondaryToken
			str.Val = self.lexical_analyser.GetStringConstant(self.lexical_analyser.SecondaryToken)

			STRStatic.type = NonTerminal.STR
			STRStatic.attribute = str

			self.push(STRStatic)
			pass

		elif RuleS.NUM0: # NUM -> n
			num = NUMStatic.attribute
			num.type = stringObj
			num.Pos = self.lexical_analyser.SecondaryToken
			num.Val = self.lexical_analyser.GetNumeralConstant(self.lexical_analyser.SecondaryToken)

			NUMStatic.type = NonTerminal.NUM
			NUMStatic.attribute = num

			self.push(NUMStatic)
			pass

		elif RuleS.NB0: # NB -> ''
			self.scope.new_block()
			pass

		elif RuleS.MF0: # MF -> ''
			TStatic = self.top()
			self.pop()
			LPStatic = self.top()
			self.pop()
			IDDStatic = self.top()
			self.pop()

			f = IDDStatic.attribute.Object
			ts = TStatic.attribute
			lp = LPStatic.attribute

			f.kind = Kind.KindFunction
			funct = f.T
			funct.PRetType = ts.type
			funct.PParams = lp.List
			funct.Params = LPStatic.size
			funct.Vars = 0
			f.T = funct
			curFunction = f

			self.output_file.write("BEGIN_FUNC %d, %d, %02d\n", funct.Index, funct.Params, 0)
			# pos, _ = self.output_file.seek(0, os.SEEK_CUR)
			# functionVarPos = int(pos) - 3
			pass

		elif RuleS.MC0: # MC -> ''
			IDUStatic = self.top()
			f = IDUStatic.attribute.Object

			mc = MCStatic.attribute
			if f.kind != Kind.KindFunction:
				mc.type = universalObj
				mc.Param = None
				mc.Err = 1
				# err ?
			else:
				mc.type = f.T.PRetType
				mc.Param = f.T.PParams
				mc.Err = 0
			

			MCStatic.attribute = mc
			MCStatic.type = NonTerminal.MC

			self.push(MCStatic)
			pass

		elif RuleS.NF0: # NF -> ''
			IDDStatic = self.top()

			f = IDDStatic.attribute.Object

			f.kind = Kind.KindFunction
			
			if f.T is not None:
				funct = f.t
			else:
				funct.params = 0
				funct.vars = 0
				funct.index = self.nfuncs
				self.nfuncs += 1
			
			f.T = funct

			self.scope.new_block()
			pass

		elif RuleS.MT0: # MT -> ''
			l = self.label
			self.label += 1

			mt = MTStatic.attribute
			mt.Label = l

			MTStatic.attribute = mt
			MTStatic.type = NonTerminal.MT

			self.output_file.write("\tTJMP_FW L%d\n", l)

			self.push(MTStatic)
			pass

		elif RuleS.ME0: # ME -> ''
			MTStatic = self.top()
			l1 = MTStatic.attribute.Label

			l2 = self.label
			self.label += 1

			me = MEStatic.attribute
			me.Label = l2
			MEStatic.type = NonTerminal.ME

			self.output_file.write("\tTJMP_FW %d\n L%d\n", l2, l1)
			self.push(MEStatic)
			pass

		elif RuleS.MW0: # MW -> ''
			l = self.label
			self.label += 1
			mw = MWStatic.attribute
			mw.Label = l
			MWStatic.attribute = mw

			self.output_file.write("\tL%d", l)
			self.push(MWStatic)
			pass
