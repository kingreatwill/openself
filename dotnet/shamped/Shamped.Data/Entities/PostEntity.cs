using System;

namespace Shamped.Data.Entities
{
    public class PostEntity
    {
        public long PostId { get; set; }

        public long TenantId { get; set; }

        public long UniqueId { get; set; }

        public string Title { get; set; }

        public string Slug { get; set; }

        public string Author { get; set; }

        public string Content { get; set; }

        public string ContentAbstract { get; set; }

        public bool CommentEnabled { get; set; }

        public bool Published { get; set; }

        public bool Sitemaped { get; set; }

        public bool Feeded { get; set; }

        public string LanguageCode { get; set; }

     
        public string ImageUrl { get; set; }

     
        public string ThumbnailUrl { get; set; }

        public DateTime CreateAt { get; set; }

        public DateTime? PublishedAt { get; set; }

        public DateTime UpdatedAt { get; set; }

        public int Revision { get; set; }

        public bool Deleted { get; set; }
    }
}
