import pathlib

from cldfbench import Dataset as BaseDataset


class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "SegBo"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        from cldfbench import CLDFSpec
        return CLDFSpec(dir=self.cldf_dir, module='StructureDataset')

    def cmd_download(self, args):
        """
        Download files to the raw/ directory. You can use helpers methods of `self.raw_dir`, e.g.

        >>> self.raw_dir.download(url, fname)

        """
        self.raw_dir.download('https://raw.githubusercontent.com/segbo-db/segbo/master/data/segbo_with_glottolog.csv', 'segbo_with_glottolog.csv')

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """

        # Add components
        """
        args.writer.cldf.add_columns(
            "ValueTable",
            {"name": "Marginal", "datatype": "boolean"},
            {"name": "Allophones", "separator": " "},
            "Contribution_ID",
        )
        """
        # args.writer.cldf.add_component("ValueTable")
        """
        args.writer.cldf.add_component("ParameterTable")
        args.writer.cldf.add_component(
            "LanguageTable", "Family_Glottocode", "Family_Name"
        )
        """

        # Iterate over raw data
        values = []
        counter = 1

        # Read raw data
        for row in self.raw_dir.read_csv(
                'segbo_with_glottolog.csv',
                dicts=True,
        ):
            print(row)
            values.append(
                {
                    "ID": str(counter),
                    "Language_ID": row['Glottocode'],
                    "Value": row['BorrowedSound'],
                    "Source": [],  # TODO
                }
            )
            counter += 1

        # Write data and validate
        args.writer.write(
            **{
                "ValueTable": values
            }
        )

        """
        # from csvw.dsv_dialects import Dialect
        for row in self.raw_dir.read_csv(
                'segbo_with_glottolog.csv',
                dicts=True,
        ):
            print(row)
            args.writer.objects['ValueTable'].append({
                'ID': row['wals code'],
                'Language_ID': row['wals code'],
                'Parameter_ID': '1A',
                'Value': row['description'],
            })
        """