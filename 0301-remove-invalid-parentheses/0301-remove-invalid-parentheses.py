class Solution:
    def removeInvalidParentheses(self, s):
        ans = set()
        best = len(s)

        def solve(i, numberOfOpenAndClose, removedBrackets, cur):
            nonlocal best

            if numberOfOpenAndClose < 0 or removedBrackets > best:
                return

            if i == len(s):
                if numberOfOpenAndClose == 0:
                    if removedBrackets < best:
                        ans.clear()
                        best = removedBrackets
                    ans.add("".join(cur))
                return

            if s[i].isalpha():
                cur.append(s[i])
                solve(i + 1, numberOfOpenAndClose, removedBrackets, cur)
                cur.pop()

            elif s[i] == '(':
                cur.append('(')
                solve(i + 1, numberOfOpenAndClose + 1, removedBrackets, cur)
                cur.pop()

                solve(i + 1, numberOfOpenAndClose, removedBrackets + 1, cur)

            else:
                if numberOfOpenAndClose > 0:
                    cur.append(')')
                    solve(i + 1, numberOfOpenAndClose - 1, removedBrackets, cur)
                    cur.pop()

                solve(i + 1, numberOfOpenAndClose, removedBrackets + 1, cur)

        solve(0, 0, 0, [])

        return list(ans)