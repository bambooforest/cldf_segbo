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
        self.raw_dir.download('https://wals.info/feature/1A.tab', '1A.tsv')

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """
        from csvw.dsv_dialects import Dialect
        for row in self.raw_dir.read_csv(
                '1A.tsv',
                dicts=True,
                dialect=Dialect(
                    skipRows=5,  # Ignore the citation info on top
                    skipBlankRows=True,
                    delimiter='\t',
                )
        ):
            print(row)
            args.writer.objects['ValueTable'].append({
                'ID': row['wals code'],
                'Language_ID': row['wals code'],
                'Parameter_ID': '1A',
                'Value': row['description'],
            })