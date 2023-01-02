This package is all in one text preprocessing pipeline and takes text input in the form of pandas series and outputs as pandas series object.

**All the text_processing sub-functions may be viewed here**
https://github.com/tariqjamil-bwp/pypi_projects/tree/main/tj_nlp


**Installing:**
pip install -i https://test.pypi.org/simple/ tj-preproc

**Usage:** (by example)
from tj_text.tj_preproc import text_preprocessing_ds, text_preprocessing

df2 = df1.copy()
df2['input_data'] = text_preprocessing_ds(df2['Phrase'])

**Note:** It will not work with .apply(text_....) method, as .apply is item by item processing which may not be optimized at dataframe level.


**Details**:
It has a variety of input flags, controlling the appropritae text preprocessing activity, and are by default set to True.
The details of flags is as under:

** The function is optimized to take advantage of the multi threaded processors **

**Arguments:**
1. pdSeries: A positional argument, of pandas series object type, and should contain text phrases to be preprocessed

    
** All following arguments are key-word type ** 

 2. NewLine removal:
    Parameter: 'newlines_tabs'
    This setting when enablesd causes the function to remove all the occurrences of newlines, tabs, and combinations like: \\n, \\.
    
    Example:
    Input : This is her \\ first day at this place.\n Please,\t Be nice to her.\\n
    Output : This is her first day at this place. Please, Be nice to her. 
    

3. HTML Tags
    Parameter: 'remove_html'
    This setting when enablesd causes the function to remove all the occurrences of html tags from the text.
    
    Example:
    Input : This is a nice place to live. 
    Output : This is a nice place to live.  
    

4. Hyper Links removal
    This setting when enablesd causes the function to remove all the occurrences of links.
    Parameter: 'links'

    Example:
    Input : To know more about cats and food & website: catster.com  visit: https://catster.com//how-to-feed-cats
    Output : To know more about cats and food & website: visit:     
    

5. Removing extra white spaces
    Parameter: 'extra_whitespace' 
    This setting when enablesd causes the function to remove extra whitespaces from the text
        
    Example:
    Input : How   are   you   doing   ?
    Output : How are you doing ?     

    
6. Accented Characters Removal:
    Parameter: 'accented_chars' 
    This setting when enablesd causes the function to remove accented characters from the text contained within the Dataset.
               
    Example:
    Input : Málaga, àéêöhello
    Output : Malaga, aeeohello    


7. Lower Casing
    Parameter: 'lowercase'
    This setting when enablesd causes the function to convert text into lower case.
             
    Example:
    Input : The World is Full of Surprises!
    Output : the world is full of surprises!
    

8. Removing Character Repetitions:
    Parameter: 'repeatition'
    This setting when enablesd causes the function to reduce repeatition to two characters for alphabets and to one character for punctuations.
            
    Example:
    Input : Realllllllllyyyyy,        Greeeeaaaatttt   !!!!?....;;;;:)
    Output : Reallyy, Greeaatt !?.;:)
    
    
9. Expand Contractions:
    Parameter: 'contractions'
    This setting when enablesd causes the function to expand shortened words to the actual form.
       e.g. don't to do not
    
       Example: 
       Input : ain't, aren't, can't, cause, can't've
       Output :  is not, are not, cannot, because, cannot have 


10. Removing Special Characters
    Parameter: 'special_chars'
    This setting when enablesd causes the function to remove all the special characters except a preset list of characters as they have imp meaning in the text provided.
       
    Example: 
    Input : Hello, T-a-r-i-q. Thi*s is $100.05 : the payment that you will recieve! (Is this okay?) 
    Output :  Hello, Tariq. This is $100.05 : the payment that you will recieve! Is this okay?
       

11. Removong Stop Words
    Parameter: 'stop_words'
    This setting when enablesd causes the function to remove the stopwords which doesn't add much meaning to a sentence 
    & they can be remove safely without comprimising meaning of the sentence.
            
    Example: 
    Input : This is Tariq from karachi who came here to study.
    Output : ["'This", 'Tariq', 'karachi', 'came', 'study', '.', "'"] 


12. Mis-spelled words Correction:
    Parameter: 'mis_spell'
    This setting when enablesd causes the function to correct spellings. Currently only English language is supported.
 
    Example: 
    Input : This is OAkbar from Londn who came heree to studdy.
    Output : This is Akbar from London who came here to study.
      

13. Lamentization:
    Parameters: 'lemmatization_allow'
    This setting when enablesd causes the function to converts word to their root words without explicitely cut down as done in stemming.
            
    Example: 
    Input : text reduced 
    Output :  text reduce