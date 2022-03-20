class Solution(object):

    def fullJustify(self, words, maxWidth):
        curr_line = []
        curr_line_width = 0
        lines = []
        spaces = 0
        
        for word in words:
            
            if len(word) + curr_line_width + len(curr_line) > maxWidth:
                
                if len(curr_line)-1:
                    spaces = len(curr_line) - 1
                else:
                    spaces = 1

                for i in range(maxWidth - curr_line_width):
                    curr_line[i % nspaces] += " "

                lines.append("".join(curr_line))
                curr_line = []
                curr_line_width = 0

            curr_line.append(word)
            curr_line_width += len(word)
        
        last_line = " ".join(curr_line)
        last_line = last_line.strip()
        last_line = last_line + " "*(maxWidth - len(last_line))
        lines.append(last_line)
        
        return lines