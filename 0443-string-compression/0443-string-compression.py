class Solution:
    def compress(self, chars: List[str]) -> int:

        write = 0  # Position to write in the array

        read = 0  # Position to read from the array

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count occurrences of the current character
            while read < len(chars) and chars[read] == char:
                count += 1
                read += 1

            # Write the character
            chars[write] = char
            write += 1

            # If the count is greater than 1, write its digits
            if count > 1:
                for digit in str(count):  # Convert number to string and write each digit
                    chars[write] = digit
                    write += 1

        return write  # The new length of the modified array
