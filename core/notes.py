class Note:
    def __init__(self, path: str, quiz_frequency: float, file_frequency: float,) -> None:
        self.path = path
        self.normal_ranges: dict[str, tuple[float, float]] = dict()

        self.line_counter = 0
        self.quiz_frequency = quiz_frequency
        self.new_file_frequency = file_frequency

    def main_file(self) -> str:
        if '.csv' in self.path:
            return ''

        return f'{self.path}\\out.csv'


if __name__ == '__main__':
    pass
