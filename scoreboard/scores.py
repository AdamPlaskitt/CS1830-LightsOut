import os
from scoreboard._connect import connect

THIS_DIR = os.path.dirname(os.path.abspath(__file__))
NAME = 'scoreboard.txt'
LOCATION = '{this_dir}{connector}{name}'.format(this_dir=THIS_DIR, connector='/', name=NAME)


class Scores:
    def get_scores(self):
        """
        :return: title, list_of_scores
        """
        list_scores = []
        title = 'ERROR'
        #  attempt to open google sheets connection
        try:
            google = connect()
            list_google_scores = google.get_all_values()
            title = 'Online'
            for score in list_google_scores:
                try:
                    # ensure int
                    score[0] = int(score[0])
                # handle errors
                except TypeError:
                    pass
                except Exception as e:
                    print(e)
                # append to list of scores
                list_scores.append(score)
        except ImportError:
            pass
        except ConnectionError:
            pass
        except Exception as e:  # unknown error
            print(e)
        # if google connection failed, attempt local connection
        if not list_scores:
            try:
                file = open(LOCATION)
                for line in file:
                    content = line.strip('\n')
                    score = content.split('/')
                    try:
                        score[0] = int(score[0])
                    except TypeError:
                        pass
                    except Exception as e:
                        print(e)
                    # append scores to list of scores
                    list_scores.append(score)
                title = 'Local'
            # handle errors
            except FileNotFoundError:
                pass
            except Exception as e:
                print(e)
            finally:
                try:
                    # close local file
                    file.close()
                except UnboundLocalError:
                    pass
                except Exception as e:
                    print(e)
        # if both failed return ERROR
        if not list_scores:
            list_scores.append('ERROR')
        return title, list_scores

    def add_score(self, new_score, name='ANONYMOUS'):
        """
        add a score to a scoreboard
        :type name: string
        :type score: int
        :return:
        """
        list_scores = []
        # update google sheets scoreboard
        # attempt google sheets connection
        try:
            google = connect()
            list_google_scores = google.get_all_values()
            for score in list_google_scores:
                try:
                    score[0] = int(score[0])
                except TypeError:
                    pass
                except Exception as e:
                    print(e)
                # append scores to list of scores
                list_scores.append(score)
        except ImportError:
            pass
        except ConnectionError:
            pass
        except Exception as e:  # unknown error
            print(e)
        # added score to list in sorted manner
        try:
            sorted_scores = self._insert_score(list_scores, [new_score, name])
        except Exception as e:
            print(e)
        for i in range(len(sorted_scores)):
            for j in range(2):
                google.update_cell(i+1, j+1, sorted_scores[i][j])
                # TODO, needs to be optimised, items that are still in the same position can be ignored

        list_scores = []
        # update local scoreboard
        # read current scoreboard in file
        try:
            file = open(LOCATION)
            for line in file:
                content = line.strip('\n')
                score = content.split('/')
                try:
                    score[0] = int(score[0])
                except TypeError:
                    pass
                except Exception as e:
                    print(e)
                # append scores to list of scores
                list_scores.append(score)
        # handle errors
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
        finally:
            try:
                # close local file
                file.close()
            except UnboundLocalError:
                pass
            except Exception as e:
                print(e)

        # write to file
        try:
            file = open(LOCATION, 'w')
            # sort
            for i in range(len(sorted_scores)):
                content = '{score}{conn}{name}{line}'.format(score=sorted_scores[i][0], conn='/',
                                                             name=sorted_scores[i][1], line='\n')
                file.write(content)
                # TODO, needs to be optimised, items that are still in the same position can be ignored
        # handle errors
        except FileNotFoundError:
            pass
        except Exception as e:
            print(e)
        finally:
            try:
                # close local file
                file.close()
            except UnboundLocalError:
                pass
            except Exception as e:
                print(e)

    def _reset_scoreboard(self, local=True):
        """
        reset a score to a scoreboard
        :param local: reset local or google scoreboard, defualt to local
        :return:
        """
        # TODO
        pass

    # add score to 2d list using insertion sort
    def _insert_score(self, list, item):
        for index in range(len(list)):
            if item[0] > list[index][0]:
                list.insert(index, item)
                break
            elif item[0] == list[index][0]:
                if item[1] < list[index][1]:
                    list.insert(index, item)
                    break
                elif item[1] == list[index][1]:
                    break
        return list


if __name__ == '__main__':
    Scores().add_score(400, 'a')
    pass
