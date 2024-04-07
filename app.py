{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7d762c59-5874-4e07-8b15-2392f475eb70",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (3072803594.py, line 2)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[1], line 2\u001b[1;36m\u001b[0m\n\u001b[1;33m    import joblib\u001b[0m\n\u001b[1;37m    ^\u001b[0m\n\u001b[1;31mIndentationError\u001b[0m\u001b[1;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template  \n",
    " import joblib  \n",
    " import sklearn  \n",
    " import pickle, gzip  \n",
    " import pandas as pd  \n",
    " import numpy as np  \n",
    " app = Flask(__name__)  \n",
    " model = joblib.load('Heart_Disease_Prediction.pkl')  \n",
    " @app.route('/')  \n",
    " def home():  \n",
    "   return render_template(\"home.html\")  \n",
    " @app.route(\"/predict\", methods=[\"POST\"])  \n",
    " def predict():  \n",
    "   age = request.form[\"age\"]  \n",
    "   sex = request.form[\"sex\"]  \n",
    "   trestbps = request.form[\"trestbps\"]  \n",
    "   chol = request.form[\"chol\"]  \n",
    "   oldpeak = request.form[\"oldpeak\"]  \n",
    "   thalach = request.form[\"thalach\"]  \n",
    "   fbs = request.form[\"fbs\"]  \n",
    "   exang = request.form[\"exang\"]  \n",
    "   slope = request.form[\"slope\"]  \n",
    "   cp = request.form[\"cp\"]  \n",
    "   thal = request.form[\"thal\"]  \n",
    "   ca = request.form[\"ca\"]  \n",
    "   restecg = request.form[\"restecg\"]  \n",
    "   arr = np.array([[age, sex, cp, trestbps,  \n",
    "            chol, fbs, restecg, thalach,  \n",
    "            exang, oldpeak, slope, ca,  \n",
    "            thal]])  \n",
    "   pred = model.predict(arr)  \n",
    "   if pred == 0:  \n",
    "     res_val = \"NO HEART PROBLEM\"  \n",
    "   else:  \n",
    "     res_val = \"HEART PROBLEM\"  \n",
    "   return render_template('home.html', prediction_text='PATIENT HAS {}'.format(res_val))  \n",
    " if __name__ == \"__main__\":  \n",
    "   app.run(debug=True)  "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ec2f71a-4425-4af6-8345-ac28c89bb7a9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, render_template, request \n",
    "import joblib\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('home.html')\n",
    "\n",
    "\n",
    "@app.route(\"/predict\", methods=['GET','POST'])\n",
    "def predict():\n",
    "    if request.method == 'POST':\n",
    "        age = float(request.form['age'])\n",
    "        sex = float(request.form['sex'])\n",
    "        cp = float(request.form['cp'])\n",
    "        trestbps = float(request.form['trestbps'])\n",
    "        chol = float(request.form['chol'])\n",
    "        fbs= float(request.form['fbs'])\n",
    "        restecg = float(request.form['restecg'])\n",
    "        thalach = float(request.form['thalach'])\n",
    "        exang = float(request.form['exang'])\n",
    "        oldpeak = float(request.form['oldpeak'])\n",
    "        slope = float(request.form['slope'])\n",
    "        ca = float(request.form['ca'])\n",
    "        thal = float(request.form['thal'])\n",
    "\n",
    "        pred_args = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]\n",
    "\n",
    "        mul_reg = open('heart_svm_13.pkl','rb')\n",
    "        ml_model = joblib.load(mul_reg)\n",
    "        model_predcition = ml_model.predict([pred_args])\n",
    "        if model_predcition == 1:\n",
    "            res = 'Affected'\n",
    "        else:\n",
    "            res = 'Not affected'\n",
    "        #return res\n",
    "    return render_template('home.html', prediction = res)\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cde1c23f-f12e-40ba-bf71-96616bb2b1cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
