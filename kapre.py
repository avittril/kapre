<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kalkulator Konstanta Kaprekar 🔢</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .kaprekar-gradient {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .result-card {
            background-color: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
        }
        /* Animasi sederhana untuk hasil */
        .step-item {
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInSlideUp 0.5s ease-out forwards;
        }
        @keyframes fadeInSlideUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap" rel="stylesheet">
</head>
<body class="kaprekar-gradient min-h-screen flex flex-col items-center justify-center p-4 text-white">

    <div class="bg-white/90 text-gray-800 p-8 rounded-xl shadow-2xl w-full max-w-md transform transition-all hover:scale-105 duration-300">
        <h1 class="text-3xl font-bold text-center mb-2 text-transparent bg-clip-text bg-gradient-to-r from-purple-600 to-pink-600">Kalkulator Kaprekar</h1>
        <p class="text-center text-gray-600 mb-6">Temukan keajaiban Konstanta Kaprekar (6174 atau 495)!</p>

        <div class="mb-4">
            <label for="numberInput" class="block text-sm font-medium text-gray-700 mb-1">Masukkan Angka (3 atau 4 digit):</label>
            <input type="text" id="numberInput" name="numberInput"
                   class="mt-1 block w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm"
                   placeholder="Contoh: 3524 atau 182">
        </div>

        <button id="calculateButton"
                class="w-full kaprekar-gradient text-white font-semibold py-3 px-4 rounded-lg shadow-md hover:opacity-90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 transition-transform transform hover:scale-105 duration-200">
            ✨ Hitung Keajaiban ✨
        </button>

        <div id="loadingIndicator" class="hidden text-center mt-4">
            <svg class="animate-spin h-8 w-8 text-indigo-600 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <p class="text-indigo-600 mt-2">Menghitung...</p>
        </div>
        
        <div id="resultArea" class="mt-6">
            </div>
    </div>

    <footer class="mt-8 text-center text-sm text-white/70">
        <p>Dibuat dengan keajaiban matematika oleh AI.</p>
    </footer>

    <script>
        const numberInput = document.getElementById('numberInput');
        const calculateButton = document.getElementById('calculateButton');
        const resultArea = document.getElementById('resultArea');
        const loadingIndicator = document.getElementById('loadingIndicator');

        calculateButton.addEventListener('click', () => {
            const inputValue = numberInput.value.trim();
            resultArea.innerHTML = ''; // Bersihkan hasil sebelumnya
            loadingIndicator.classList.remove('hidden'); // Tampilkan loading

            // Tambahkan sedikit delay untuk efek loading yang lebih terlihat
            setTimeout(() => {
                processKaprekar(inputValue);
                loadingIndicator.classList.add('hidden'); // Sembunyikan loading
            }, 500); 
        });
        
        numberInput.addEventListener('keypress', (event) => {
            if (event.key === 'Enter') {
                calculateButton.click();
            }
        });

        function displayError(message) {
            resultArea.innerHTML = `<div class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg shadow" role="alert">
                                        <span class="font-medium">❌ Error:</span> ${message}
                                    </div>`;
        }

        function displayResult(steps, finalMessage, iterationCount) {
            let htmlOutput = '<h3 class="text-xl font-semibold mb-3 text-gray-700">Langkah Iterasi:</h3>';
            htmlOutput += '<div class="space-y-2">';

            steps.forEach((step, index) => {
                // Tambahkan delay animasi untuk setiap item
                htmlOutput += `<div class="p-3 result-card rounded-lg shadow text-gray-700 bg-white/80 step-item" style="animation-delay: ${index * 0.1}s;">${step}</div>`;
            });
            
            htmlOutput += '</div>';
            htmlOutput += `<div class="mt-6 p-4 text-green-700 bg-green-100 rounded-lg shadow" role="alert">
                               <p class="font-bold text-lg">${finalMessage}</p>
                               <p>Total iterasi yang dibutuhkan: <span class="font-bold">${iterationCount}</span> langkah.</p>
                           </div>`;
            resultArea.innerHTML = htmlOutput;
        }

        function processKaprekar(numStr) {
            // --- Validasi Input ---
            if (!/^\d+$/.test(numStr)) {
                displayError("Input tidak valid. Harap masukkan angka saja.");
                return;
            }

            if (numStr.length !== 3 && numStr.length !== 4) {
                displayError("Harap masukkan angka dengan panjang 3 atau 4 digit.");
                return;
            }

            if (new Set(numStr.split('')).size < 2) {
                displayError(`Angka '${numStr}' tidak valid. Minimal harus ada 2 digit yang berbeda (contoh: bukan 111 atau 4444).`);
                return;
            }

            let currentNumStr = numStr;
            const digitLength = numStr.length;
            const targetConstant = (digitLength === 4) ? 6174 : 495;
            let iterations = 0;
            const maxIterations = 10; // Batas aman, biasanya 7 untuk 4-digit
            const steps = [];

            while (parseInt(currentNumStr) !== targetConstant && iterations < maxIterations) {
                iterations++;

                // Mengubah string menjadi array digit untuk diurutkan
                let digits = currentNumStr.split('');

                // Angka terbesar
                let descendingStr = [...digits].sort((a, b) => b.localeCompare(a)).join('');
                // Angka terkecil
                let ascendingStr = [...digits].sort((a, b) => a.localeCompare(b)).join('');
                
                let numDescending = parseInt(descendingStr);
                let numAscending = parseInt(ascendingStr);

                let result = numDescending - numAscending;
                
                steps.push(`Iterasi ${iterations}: <span class="font-mono">${descendingStr}</span> - <span class="font-mono">${ascendingStr}</span> = <span class="font-mono font-semibold">${result}</span>`);

                currentNumStr = String(result).padStart(digitLength, '0'); // Pastikan panjang digit tetap

                if (parseInt(currentNumStr) === targetConstant) {
                    break;
                }
            }

            if (parseInt(currentNumStr) === targetConstant) {
                displayResult(steps, `✅ Konstanta Kaprekar (${targetConstant}) berhasil ditemukan!`, iterations);
            } else {
                steps.push("Proses dihentikan karena melebihi batas iterasi maksimum atau terjadi kesalahan.");
                displayResult(steps, `⚠️ Tidak dapat mencapai konstanta setelah ${iterations} iterasi.`, iterations);
            }
        }
    </script>
</body>
</html>
