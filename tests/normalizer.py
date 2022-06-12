import re


class Normalizer:
    def __init__(self):
        self.id1_pattern = re.compile(r"'[a-f0-9]{7}'", flags=re.MULTILINE)
        self.id2_pattern = re.compile(r"\"[a-f0-9]{7}\"", flags=re.MULTILINE)

    def normalize_id(self, output):
        normalized_output = output
        normalized_output = self.id1_pattern.sub("id", normalized_output)
        normalized_output = self.id2_pattern.sub("id", normalized_output)
        return normalized_output

    def normalize_output(self, output, start_index=0):
        output_items = []
        for block in output.call_args_list[start_index:]:
            output_items.append(block.args[0])
        return self.normalize_id("\n".join(output_items)).strip()
