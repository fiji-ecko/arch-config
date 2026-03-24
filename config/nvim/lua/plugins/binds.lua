return {{
  "max397574/better-escape.nvim",
  event = "InsertEnter",
  config = function()
    require("better_escape").setup({
      mapping = { "j", "k" }, 
      timeout = 200,
      clear_empty_lines = false, 
      keys = "<Esc>",          
    })
  end,
}}
