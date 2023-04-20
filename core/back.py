from notes import Note


class CSVParser:
    def __init__(self, note: Note) -> None:
        self.note = note

    def get_parameters(self) -> list[str]:
        first_file = self.get_files()[0]
        return open(f'{self.note.path}//{first_file}').readline().split(';')

    def get_files(self) -> list[str]:
        main_file = open(f'{self.note.path}\\{self.note.main_file()}.csv').readlines()
        return [main_file[i].split(';')[1] for i in range(len(main_file))]

    def get_parameter_values(self, parameter: str, file_name: str) -> list[float]:
        params = self.get_parameters()
        index = params.index(parameter) if parameter in params else -1

        if file_name not in self.get_files() or index == -1:
            return []

        log = open(f'{self.note.path}\\{file_name}').readlines()[1:]
        return [float(log[i].split(';')[index]) for i in range(len(log))]

    def take_last_file(self, parameter: str) -> list[float]:
        pass

    def take_last_note(self, parameter: str) -> float:
        return self.take_last_file(parameter)[-1]


class Checker:
    def __init__(self, parser: CSVParser) -> None:
        self.parser = parser
        self.parameters = self.parser.get_parameters()

    def set_norm_ranges(self, ranges: dict[str, tuple[float, float]]) -> None:
        for param in ranges:
            if param in self.parser.note.normal_ranges:
                self.parser.note.normal_ranges[param] = ranges[param]

    def check(self) -> bool:
        for param in self.parameters:
            if self.parser.take_last_note(param) <= self.parser.note.normal_ranges[param][0] or \
                    self.parser.take_last_note(param) >= self.parser.note.normal_ranges[param][1]:
                return False

        return True

    def error_message(self, parameter: str) -> str:
        if parameter not in self.parameters:
            return 'okay'

        return f'{parameter} is out of normal range'


if __name__ == '__main__':
    csv = CSVParser('C:\\Users\\Damir\\Desktop\\.phys', 'out.csv')
