return {{
    "neovim/nvim-lspconfig",
    dependencies = {
      "williamboman/mason.nvim",
      "williamboman/mason-lspconfig.nvim",
      "hrsh7th/nvim-cmp",
      "hrsh7th/cmp-nvim-lsp",
      "hrsh7th/cmp-buffer",
      "hrsh7th/cmp-path",
      "L3MON4D3/LuaSnip",
    },
    config = function()
      -- Mason для установки LSP серверов
      require("mason").setup()
      require("mason-lspconfig").setup({
        ensure_installed = { "pyright" },
        automatic_installation = true,
      })

      -- Настройка nvim-cmp (автодополнение)
      local cmp = require("cmp")
      local cmp_lsp = require("cmp_nvim_lsp")
      
      cmp.setup({
        snippet = {
          expand = function(args)
            require("luasnip").lsp_expand(args.body)
          end,
        },
        mapping = cmp.mapping.preset.insert({
          ["<C-b>"] = cmp.mapping.scroll_docs(-4),
          ["<C-f>"] = cmp.mapping.scroll_docs(4),
          ["<C-Space>"] = cmp.mapping.complete(),
          ["<C-e>"] = cmp.mapping.abort(),
          ["<CR>"] = cmp.mapping.confirm({ select = true }),
          ["<Tab>"] = cmp.mapping(function(fallback)
            if cmp.visible() then
              cmp.select_next_item()
            else
              fallback()
            end
          end, { "i", "s" }),
        }),
        sources = cmp.config.sources({
          { name = "nvim_lsp" },
          { name = "buffer" },
          { name = "path" },
        }),
      })

      -- Новый API для Neovim 0.11+
      -- Сначала определяем конфигурацию для pyright
      vim.lsp.config.pyright = {
        cmd = { "pyright-langserver", "--stdio" },
        filetypes = { "python" },
        root_markers = { "pyproject.toml", "setup.py", "setup.cfg", "requirements.txt", ".git" },
        settings = {
          python = {
            analysis = {
              typeCheckingMode = "basic",
              autoSearchPaths = true,
              useLibraryCodeForTypes = true,
            },
          },
        },
        capabilities = cmp_lsp.default_capabilities(),
      }

      -- Затем включаем LSP для всех настроенных серверов
      vim.lsp.enable("pyright")

      -- Клавиши для LSP (работают с новым API)
      vim.keymap.set("n", "gd", function() vim.lsp.buf.definition() end, { desc = "Go to definition" })
      vim.keymap.set("n", "K", function() vim.lsp.buf.hover() end, { desc = "Hover documentation" })
      vim.keymap.set("n", "gi", function() vim.lsp.buf.implementation() end, { desc = "Go to implementation" })
      vim.keymap.set("n", "gr", function() vim.lsp.buf.references() end, { desc = "Show references" })
      vim.keymap.set("n", "<leader>rn", function() vim.lsp.buf.rename() end, { desc = "Rename" })
      vim.keymap.set("n", "<leader>ca", function() vim.lsp.buf.code_action() end, { desc = "Code action" })
    end,
  },
}
