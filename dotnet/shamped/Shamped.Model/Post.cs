using System;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Shamped.Model
{
    public class Post
    {
        [Description("Post ID")]
        [Column("post_id")]
        public long PostId { get; set; }

        [Description("租户ID")]
        [Column("tenant_id")]
        public long TenantId { get; set; }

        [Description("加密ID")]
        [Column("unique_id")]
        public long UniqueId { get; set; }

        [Description("Post标题")]
        [Column("title")]
        [MaxLength(50)]
        [Required]
        public string Title { get; set; }

        [Description("静态链接")]
        [Column("slug")]
        [MaxLength(50)]
        public string Slug { get; set; }

        [Description("Post作者")]
        [Column("author")]
        [MaxLength(50)]
        public string Author { get; set; }

        [Description("Post内容")]
        [Column("content")]
        public string Content { get; set; }

        [Description("Post摘要")]
        [Column("content_abstract")]
        [MaxLength(500)]
        public string ContentAbstract { get; set; }

        [Description("是否开启评论")]
        [Column("comment_enabled")]
        public bool CommentEnabled { get; set; }

        [Description("是否已发布")]
        [Column("published")]
        public bool Published { get; set; }

        [Description("是否包含到SiteMap")]
        [Column("sitemaped")]
        public bool Sitemaped { get; set; }

        [Description("是否添加RSS")]
        [Column("feeded")]
        public bool Feeded { get; set; }

        [Description("语言")]
        [Column("language_code")]
        [MaxLength(50)]
        public string LanguageCode { get; set; }

        //public Tag[] Tags { get; set; }
        //public Category[] Categories { get; set; }
        [Description("图片")]
        [Column("image_url")]
        [MaxLength(500)]
        public string ImageUrl { get; set; }

        [Description("图片略图")]
        [Column("thumbnail_url")]
        [MaxLength(500)]
        public string ThumbnailUrl { get; set; }

        [Description("创建时间")]
        [Column("created_at")]
        public DateTime CreateAt { get; set; }

        [Description("发布时间")]
        [Column("published_at")]
        public DateTime? PublishedAt { get; set; }

        [Description("更新时间")]
        [Column("updated_at")]
        public DateTime UpdatedAt { get; set; }

        [Description("修订版本")]
        [Column("revision")]
        public int Revision { get; set; }

        [Description("是否已删除")]
        [Column("deleted")]
        public bool Deleted { get; set; }
    }
}
