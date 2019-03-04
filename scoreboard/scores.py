import os
from scoreboard._connect import connect

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
NAME = 'scoreboard1.txt'
LOCATION = '{this_dir}{connector}{name}'.format(this_dir=THIS_DIR, connector='/', name=NAME)


class Scores:
    def get_scores(self):
        """
        :return: title, list_of_scores
        """
        list_scores = []
        title = 'ERROR'
        try:
            #google = connect()
            list_scores = google.get_all_values()
            title = 'Online'
        except ImportError:
            pass
        except ConnectionError:
            pass
        except Exception as e:  # unknown error
            print(e)
        if not list_scores:
            try:
                file = open(LOCATION)
                for line in file:
                    content = line.strip('\n')
                    list_scores.append(content.split('/'))
                title = 'Local'
            except FileNotFoundError:
                pass
            except Exception as e:
                print(e)
            finally:
                try:
                    file.close()
                except UnboundLocalError:
                    pass
                except Exception as e:
                    print(e)
        if not list_scores:
            list_scores.append('ERROR')
        return title, list_scores

    def add_score(self, score, name='ANONYMOUS'):
        """
        add a score to a scoreboard
        :type name: string
        :type score: int
        :return:
        """
        # TODO
        pass

    def _reset_scoreboard(self, local=True):
        """
        reset a score to a scoreboard
        :param local: reset local or google scoreboard, defualt to local
        :return:
        """
        # TODO
        pass

if __name__ == '__main__':
    x, y = Scores().get_scores()
    print(x)