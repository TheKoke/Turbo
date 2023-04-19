class CSVParser:
    def __init__(self, path: str, main_name: str) -> None:
        self.path = path
        self.main_name = main_name

    def get_parameters(self) -> list[str]:
        first_file = self.get_files()[0]
        return open(f'{self.path}//{first_file}').readline().split(';')

    def get_files(self) -> list[str]:
        main_file = open(f'{self.path}\\{self.main_name}.csv').readlines()
        return [main_file[i].split(';')[1] for i in range(len(main_file))]

    def get_parameter_values(self, parameter: str, file_name: str) -> list[float]:
        params = self.get_parameters()
        index = params.index(parameter) if parameter in params else -1

        if file_name not in self.get_files() or index == -1:
            return []

        log = open(f'{self.path}\\{file_name}').readlines()[1:]
        return [float(log[i].split(';')[index]) for i in range(len(log))]

    def take_last_file(self, parameter: str) -> list[float]:
        pass


class Checker:
    def __init__(self, parser: CSVParser) -> None:
        """
        all frequency parameters in milliseconds
        """
        self.parser = parser
        self.norm_ranges = self.build_norm_ranges()

    def build_norm_ranges(self) -> dict[str, tuple[float, float]]:
        return {param: (0, 0) for param in self.parser.get_parameters()}

    def set_norm_ranges(self, ranges: dict[str, tuple[float, float]]) -> None:
        for param in ranges:
            if param in self.norm_ranges:
                self.norm_ranges[param] = ranges[param]

    def check(self) -> bool:
        is_ok = True
        return is_ok

    def error_message(self, parameter: str) -> str:
        pass


if __name__ == '__main__':
    csv = CSVParser('C:\\Users\\Damir\\Desktop\\.phys', 'out.csv')
