import tensorflow as tf
import gradio as gr
import pandas as pd
from tensorflow.keras.layers import TextVectorization
path="Comment Toxicity/jigsaw-toxic-comment-classification-challenge/train.csv/train.csv"
df=pd.read_csv(path)
X = df['comment_text']
y = df[df.columns[2:]].values
vectorizer = TextVectorization(max_tokens=200000,
                               output_sequence_length=1800,
                               output_mode='int')

vectorizer.adapt(X.values)
vectorized_text = vectorizer(X.values)

# Load the model
model_path = 'Comment Toxicity/Comment_Toxicity.h5'
model = tf.keras.models.load_model(model_path)

def score_comment(comment):
    vectorized_comment = vectorizer([comment])
    results = model.predict(vectorized_comment)

    text = ''
    for idx, col in enumerate(df.columns[2:]):
        text += '{}: {}\n'.format(col, results[0][idx]>0.5)

    return text

interface = gr.Interface(fn=score_comment,
                         inputs=gr.inputs.Textbox(lines=2, placeholder='Comment to score'),
                        outputs='text')

interface.launch(share=True)
