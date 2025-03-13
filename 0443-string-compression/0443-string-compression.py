class Solution:
    def compress(self, chars: List[str]) -> int:
        write = read = 0

        while read < len(chars):
            count = 0
            curr_char = chars[read]

            # increment count while still on same character
            while read < len(chars) and curr_char == chars[read]:
                count += 1
                read += 1

            # write the character to our list
            chars[write] = curr_char
            write += 1

            # append group length to char if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        return write

            
