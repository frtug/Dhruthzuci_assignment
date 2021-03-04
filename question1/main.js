const express = require('express');
const app = express();

const port = 3000;

app.use(express.urlencoded({ extended: false }));
app.use(express.json())


app.post('/find_symbols_in_names', (req, res) => {
    data = req.body
    const chem = data.chemicals;
    const sym = data.symbols;
    const result = [];
    var i=0;
    chem.map((chemicals) =>{
        sym.map((symbol) =>{
            if(chemicals.includes(symbol)){
                var pos = chemicals.indexOf(symbol);
                var end = pos + symbol.length -1
                str =  chemicals.slice(0,pos)+ "[" + chemicals.slice(pos,end+1) +"]" + chemicals.slice(end+1,chemicals.length);

                result[i] = str;
                i++;
            }
        })
    })
    console.log(result)
    res.status(200).send("Done");
});

app.listen(port, () => console.log(`post request ${port}!`))
