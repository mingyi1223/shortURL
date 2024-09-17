function urlShortener() {
    return {
        longUrl: '',
        shortUrl: '',
        shortCode: '',
        longUrlRetrieved: '',
        errorMessage: '',

        async createShortUrl() {
            this.errorMessage = '';
            this.shortUrl = '';

            try {
                const response = await fetch('http://localhost:8000/shortener/', { 
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ long: this.longUrl })
                });
                if (response.ok) {
                    const data = await response.json();
                    this.shortUrl = data.short;
                } else {
                    const errorData = await response.json();
                    this.errorMessage = errorData.detail || 'Error creating short URL';
                }
            } catch (error) {
                this.errorMessage = 'Network error';
            }
        },

        async retrieveLongUrl() {
            this.errorMessage = '';
            this.longUrlRetrieved = '';

            try {
                const response = await fetch(`http://localhost:8000/shortener/${this.shortCode}/`);
                if (response.ok) {
                    const data = await response.json();
                    this.longUrlRetrieved = data.long;
                } else {
                    const errorData = await response.json();
                    this.errorMessage = errorData.detail || 'Error retrieving original URL';
                }
            } catch (error) {
                this.errorMessage = 'Network error';
            }
        }
    }
}
