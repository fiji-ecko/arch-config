return {
  {
    "Mofiqul/dracula.nvim",
    priority = 1000, -- Загружается первой
    config = function()
      vim.cmd.colorscheme("dracula")
    end,
  }
}
