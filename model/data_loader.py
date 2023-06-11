import pandas as pd
import numpy as np
from model.var_from_cfg import book_hist_path, book_rate_path,\
                        users_info_path, items_info_path



class DataLoader:
    def __init__(self):
        """
         Read and process data from .dat file and add to DataLoader property
         Handle some invalid values cases when input data
        """

        # read data from .dat file
        self.book_hist_df = self.data_reader(book_hist_path)
        self.book_rate_df = self.data_reader(book_rate_path)
        self.users_info_df = self.data_reader(users_info_path)
        self.items_info_df = self.data_reader(items_info_path)

        # all process data
        self.handle_data_process()

    @staticmethod
    def data_reader(file_path):
        """
         Reads data from tab delimeted file. 
         
         @param file_path - Path to file to read
         
         @return DataFrame with data from file_path and na_values
        """
        df = pd.read_csv(file_path, delimiter='\t', na_values=np.nan)

        return df
    

    def handle_users_info(self):
        """
        Fill age and users_info_df with mean age of people
        Extract country columns from location
        """

        # replace age > 90 or age < 5 with nan values (people who has age more than 90 or less than 5 usually can't rate books much)
        self.users_info_df.loc[(self.users_info_df.Age > 90) | (self.users_info_df.Age < 5), 'Age'] = np.nan

        # fill age's nan values with mean value
        self.users_info_df['Age'] = self.users_info_df['Age'].fillna(self.users_info_df['Age'].mean())

        # convert type 'Age' to integer
        self.users_info_df['Age'] = self.users_info_df['Age'].astype(int)

        # get user country
        self.users_info_df['Country'] = self.users_info_df['Location'].apply(lambda x: x.split(',')[-1].strip())


    def handle_items_info(self):
        """
         Replace some error values with correct ones
        """

        # replace some error values (input to wrong columns)
        self.items_info_df.loc[self.items_info_df['Year-Of-Publication'] == 'Hutchinson', 'Year-Of-Publication'] = 1973
        self.items_info_df.loc[self.items_info_df['Year-Of-Publication'] == 'Baldini&amp Castoldi', 'Year-Of-Publication'] = 1994
        self.items_info_df.loc[self.items_info_df['Year-Of-Publication'] == 'http://images.amazon.com/images/P/0451404874.01.THUMBZZZ.jpg', 'Year-Of-Publication'] = 1994

        self.items_info_df["Book-Author"] = self.items_info_df["Book-Author"].apply(lambda x: x.strip())


    def merge_rating_info(self):
        """
         Merge ratings from users and books into one dataframe and return the result
        """
        self.book_rate_df = self.book_rate_df.rename(columns={'user': 'User-ID',
                                                              'item': 'Book-ID'})
        self.items_info_df = self.items_info_df.rename(columns={'Book_ID': 'Book-ID'})

        user_group = self.book_rate_df.groupby("User-ID")
        item_group = self.book_rate_df.groupby("Book-ID")

        # number of ratings, average ratings of users, book
        average_user_rating = user_group["rating"].mean()
        number_of_ratings_by_user = user_group["rating"].count()
        average_book_rating = item_group["rating"].mean()
        number_of_book_ratings = item_group["rating"].count()

        average_user_rating.name = "avg_rating"
        number_of_ratings_by_user.name = "n_ratings"
        average_book_rating.name = "avg_rating"
        number_of_book_ratings.name = "n_ratings"

        # join ratings info with users info and items info
        self.users_info_df = self.users_info_df.join(number_of_ratings_by_user, on="User-ID")
        self.users_info_df = self.users_info_df.join(average_user_rating, on="User-ID")

        self.items_info_df = self.items_info_df.join(number_of_book_ratings, on="Book-ID")
        self.items_info_df = self.items_info_df.join(average_book_rating, on="Book-ID")

        # fill na values of number rating with zero
        self.users_info_df["n_ratings"] = self.users_info_df["n_ratings"].fillna(0)
        self.items_info_df["n_ratings"] = self.items_info_df["n_ratings"].fillna(0)

        # convert to integer
        self.users_info_df["n_ratings"] = self.users_info_df["n_ratings"].astype(int)
        self.items_info_df["n_ratings"] = self.items_info_df["n_ratings"].astype(int)


    def handle_data_process(self):
        """
         Process data and merge ratings into one.
        """
        self.handle_items_info()
        self.handle_users_info()
        self.merge_rating_info()



if __name__ == '__main__':
    # Check users_info_df postprocessing
    DataLoader = DataLoader()
    print(DataLoader.users_info_df.head())