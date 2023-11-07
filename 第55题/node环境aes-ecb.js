function decode(str){
    var CryptoJS = require("crypto-js");
    var KEY = 'aiding6666666666';
    var key = CryptoJS.enc.Utf8.parse(KEY);
    var decrypted = CryptoJS.AES.decrypt(str, key, {
                   // iv: iv,
                   mode: CryptoJS.mode.ECB,
                   padding: CryptoJS.pad.Pkcs7,
    });
    return decrypted.toString(CryptoJS.enc.Utf8)
}
// var str_ = "2A4w0jqbUivhDV042Ka+VbfXmH65wRwPgKTNHCnEW2hkVTAx4LzvekaBzGEikZHeLblU4KdKeP2LI/nT/Z9vFfby5lg6jI336umLu6ofyFzsHihQ/lJDwCFl7yCY3RXxe6raQF061MqSao4eZ8RUQn6dnITrmFXK4gSCDTbTnrLjUueZnyozu3rmD/XvIYvjtDENnW+T3CjW3SecHQ4x3myB33JETq0coOwn0zgdP2kMqei6MDGpsXX1wp3XqLo05ysk+Pa+rzmgrWtauWcLC5UJxL6JIiP//40bKbOnHhwTcoFdoY+a6t6EGrUDWbQB7JFdJPOLT2RMYKdKz1fiQw=="
var str_ = "2A4w0jqbUivhDV042Ka+VbfXmH65wRwPgKTNHCnEW2hkVTAx4LzvekaBzGEikZHe+htFTMrIDuMFCKUdERnynVJFarAHg4fufeYRZQTQtEclE3bYgT8P10ImYGVNtjiwDWTpI3SpH9RMDZwCL08F8oU3N+UgqLHPDwGQNT26nkK8/zX07Aaf4ZNk+x3xcOj67B4oUP5SQ8AhZe8gmN0V8T1a+JozDIKF3veiIWTEGfPk9ZKjUWuRU79X++2s0/BFWgTl68O56tMaNbENZAPcp7QxDZ1vk9wo1t0nnB0OMd5TFSBwYdKqCsrXOXPofnLDmlOrxpyfX6QI4HySxVeaqQ==\n";
console.log(decode(str_));
