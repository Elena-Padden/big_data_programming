# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
   
    def __init__(self, revision = None, author = None, date = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.datetime = date
        self.changes = changes
        self.comment = comment
    
        date_details=date.split(' ')
        self.date=date_details[0]
        self.time=date_details[1]
        self.day=date_details[3].strip('(').strip(',')
        
    def get_commit_details(self):
        return 'r' + str(self.revision) + ' by ' \
                + self.author + ' on ' \
                + self.day + ' ' + self.date + ' at ' \
                + self.time + ' with ' \
                + str(len(self.comment)) + ' comment lines and ' \
                + str(len(self.changes)) + ' changes'

# read change log into a list of lines,
# strip out spaces at the start and end of each line              	
def read_file(changes_file):
    data = [line.strip() for line in open(changes_file, 'r')]
    return data
	
# convert the list of commit lines into a list of commits

# commit lines are:
#  separator line
#  commit summary (revision|author|date|number of lines in the commit comment)
#  "changed paths:" line
#  changed paths lines 
#  blank line
#  comment lines

def get_commits(data):
	sep = 72*'-'
	commits = []
	index = 1

	while index<len(data)-1:
		try:
			# parse each of the commits and put them into a list of commits
			details = data[index].split('|')
			revision = int(details[0].strip().strip('r'))
			author = details[1].strip()
			date = details[2].strip()
			comment_line_count = int(details[3].strip().split(' ')[0])
			changes = data[index+2:data.index('',index)]
			index = data.index(sep, index)
			comment = data[index-comment_line_count:index]
			
			current_commit = Commit(revision,author,date,changes,comment)
			
			index += 1	
			commits.append(current_commit)
		except IndexError:
			break
	return commits

# make a dictionary with the number of commits counted by key
# calculate the key with a lambda function
def count_changes(by, commits):
    commit_counts = {}
    for commit in commits:
        key = by(commit)
        if key not in commit_counts:
            commit_counts[key] = 0
        commit_counts[key] += 1
    return commit_counts

# sort the changes in descending order
def sorted_counts(counts):
    return sorted(counts, key=counts.get, reverse=True)

# print the number of changes and percent of total changes sorted in descending order
def write_statistics(my_file, counts, total):
    sortedkeys = sorted_counts(counts)
    for key in sortedkeys:
        counted = counts[key]
        my_file.write(key + " : " + str(counted) + " changes, " + str(counted * 100 / total) + ' %')
        
# analyse the changes by Author, Day, Hour, Month and Year
def write_analysis(commmits, output_file):
    my_file=open(output_file, 'w')
    counts = count_changes(lambda commit: commit.author, commits)
    my_file.write("Author Statistics:\n")
    write_statistics(my_file, counts, len(commits))
    my_file.write("\n");

    counts = count_changes(lambda commit: commit.day, commits)
    my_file.write("Day Statistics:\n")
    write_statistics(my_file, counts, len(commits))
    my_file.write("\n")
    
    counts = count_changes(lambda commit: commit.time.split(':')[0], commits)
    my_file.write("Hour Statistics:\n")
    write_statistics(my_file, counts, len(commits))
    my_file.write("\n")

    counts = count_changes(lambda commit: commit.date.split('-')[1], commits)
    my_file.write("Month Statistics:\n")
    write_statistics(my_file, counts, len(commits))
    my_file.write("\n")

    counts = count_changes(lambda commit: commit.date.split('-')[0], commits)
    my_file.write("Year Statistics:\n")
    write_statistics(my_file, counts, len(commits))
    my_file.write("\n")
    my_file.close()
    
# write the changes details to a .csv file for further analysis
# include the author, original date, date, time, day, # comment lines, # files changes
def write_changes(commits, output_file):
    my_file=open(output_file, 'w')	
    my_file.write('Revision,Author,DateTime,Date,Time,Day,# Comment Lines,# Files Changed\n')
    for commit in commits :
            my_file.write(str(commit.revision) + ',' +
                            commit.author + ',"' +
                            commit.datetime + '",' +
                            commit.date + ',' +
                            commit.time + ',' +
                            commit.day + ',' +
                            str(len(commit.comment)) + ',' +
                            str(len(commit.changes)) + "\n" 
                          )
    my_file.close()


if __name__ == '__main__':
	changes_file = 'changes_python.log'
	data = read_file(changes_file)
	commits = get_commits(data)
	write_changes(commits,'changes.csv')
	write_analysis(commits,'statistics.txt')
