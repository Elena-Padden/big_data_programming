import unittest

from process_changes import Commit, read_file, get_commits, write_changes, count_changes, sorted_counts

class TestProcessChanges(unittest.TestCase):

    def setUp(self):
        testdate='2016-07-01 09:10:11 +0000 (Fri, 01 Jul 2017)'
        self.commit = Commit(1,'Tom',testdate,['1','2','3'],['Changed for','a reason'])
        self.data = read_file('changes_python.log')
        self.commits = get_commits(self.data)
        self.commit2 = Commit(2,'Kirill',testdate,[],[])

    def test_commit(self):
        self.assertEqual(1, self.commit.revision)
        self.assertEqual('Tom', self.commit.author)
        self.assertEqual('2016-07-01', self.commit.date)
        self.assertEqual('09:10:11', self.commit.time)
        self.assertEqual('Fri', self.commit.day)
        self.assertEqual(2, len(self.commit.comment))
        self.assertEqual(3, len(self.commit.changes))

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        self.assertEqual(422, len(self.commits))

    def test_first_commit(self):
        self.assertEqual('Thomas', self.commits[0].author)
        self.assertEqual(1551925, self.commits[0].revision)
        self.assertEqual(4, len(self.commits[0].changes))
        self.assertEqual(1, len(self.commits[0].comment))

    def test_count_changes(self):
        counts = count_changes(lambda commit: commit.author, [self.commit,self.commit])
        self.assertEqual(counts,{'Tom':2})

    def test_sort_changes(self):
        counts = count_changes(lambda commit: commit.author, [self.commit,self.commit2,self.commit2])
        change_order = sorted_counts(counts)
        self.assertEqual(change_order, ['Kirill','Tom'])

    def test_write_changes(self):
        write_changes([self.commit],'test_changes.csv')
        lines=read_file('test_changes.csv')
        self.assertEqual(lines[0],"Revision,Author,DateTime,Date,Time,Day,# Comment Lines,# Files Changed")
        self.assertEqual(lines[1],'1,Tom,"2016-07-01 09:10:11 +0000 (Fri, 01 Jul 2017)",2016-07-01,09:10:11,Fri,2,3')
    
if __name__ == '__main__':
    unittest.main()
