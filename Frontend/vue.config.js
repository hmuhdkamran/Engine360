module.exports = {
  lintOnSave: false,
  chainWebpack: (config) => {
    config.resolve.symlinks(false)
  }
};
