from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        fasta = request.form['fasta']
        region = request.form.get('region', 'all')
        provider_reference = request.form.get('provider_reference', '')

        # Prepare the request payload
        payload = {
            'fasta': fasta,
            'region': region,
            'provider_reference': provider_reference
        }

        # Send the payload to the synthclient API
        try:
            response = requests.post('http://localhost:80/v1/screen', json=payload)
            result = response.json()
        except requests.exceptions.RequestException as e:
            return f"An error occurred: {e}"

        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)