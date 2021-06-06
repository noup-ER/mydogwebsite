
module.exports = {
    publicPath: "./",
    configureWebpack: {
        resolve:{
            alias:{
                "router":"@/router",
                "navbar":"@/components/navbar",
                "searchbar":"@/components/searchbar",
                "titlebar":"@/components/titlebar",
                "body":"@/components/body",
                "login":"@/components/login",
                "end":"@/components/end",
                "register":"@/components/register",
                "image":"@/assets/image",
            }
        }
    }
}